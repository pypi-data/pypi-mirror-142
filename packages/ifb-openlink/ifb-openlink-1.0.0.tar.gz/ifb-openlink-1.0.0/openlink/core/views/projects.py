import logging

from django.apps import apps
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
from django.views.decorators.http import require_GET, require_POST
from guardian.decorators import permission_required_or_403
from guardian.shortcuts import assign_perm
from openlink.core.connector import Publisher
from openlink.core.filters import ProjectFilter
from openlink.core.forms import (
    LinkAssayForm,
    LinkDatasetForm,
    LinkInvestigationForm,
    LinkMappingForm,
    LinkProjectForm,
    LinkStudyForm,
    ProjectForm,
)
from openlink.core.models import Mapping, MappingProjectUser, Profile, Project, Tool
from openlink.core.views import users

logger = logging.getLogger(__name__)


@login_required
def projects(request):
    # Display all projects shared or owned by the user
    list_ids = []
    projects_list_map2 = MappingProjectUser.objects.filter(user__user=request.user)
    for proj_map in projects_list_map2:
        list_ids.append(proj_map.project.id)
    projects_list = Project.objects.filter(id__in=list_ids)
    projects_filter = ProjectFilter(request.GET, queryset=projects_list)
    return render(request, "projects/list.html", {"filter": projects_filter})


@login_required
@require_GET
def new_project(request):
    # Display an empty form to add a new project
    return render(request, "new_item/new_item.html", {"form": ProjectForm()})


@login_required
@require_POST
def add_project(request):
    # Save the project with data from the project form
    form = ProjectForm(request.POST)

    if not form.is_valid():
        # Display the same empty project form if form is not valid
        return render(request, "new_item/new_item.html", {"form": form})

    project = form.save(commit=False)
    profile = get_object_or_404(Profile, user=request.user)
    project.author = profile
    project.date_created = timezone.now()
    project.save()
    assign_perm("view_project", request.user, project)
    assign_perm("add_project", request.user, project)
    assign_perm("change_project", request.user, project)
    assign_perm("delete_project", request.user, project)
    assign_perm("manage_user", request.user, project)

    new_mappingprojectuser = MappingProjectUser()
    new_mappingprojectuser.user = get_object_or_404(Profile, user=request.user)
    new_mappingprojectuser.project = project
    new_mappingprojectuser.role = "administrator"
    new_mappingprojectuser.save()
    messages.info(request, "Project " + str(project) + " created")

    return HttpResponseRedirect(reverse("core:projects"))


def convert_to_byte(value):
    # convert octet to byte
    value_split = value.split(" ")
    try:
        nb = float(value_split[0])
    except ValueError:
        return float(0)
    byte_format = str(value_split[1])
    if byte_format == "B":
        byte_value = float(nb)
    elif byte_format == "KB":
        byte_value = float(nb * 1024)
    elif byte_format == "MB":
        byte_value = float(nb * 1024**2)
    elif byte_format == "GB":
        byte_value = float(nb * (1024**3))
    elif byte_format == "TB":
        byte_value = float(nb * (1024**4))
    elif byte_format == "PB":
        byte_value = float(nb * (1024**5))
    else:
        byte_value = float(0)
    return byte_value


def humansize(nbytes):
    # make the filesize human readable
    suffixes = ["B", "KB", "MB", "GB", "TB", "PB"]
    i = 0
    while nbytes >= 1024 and i < len(suffixes) - 1:
        nbytes /= 1024.0
        i += 1
    f = ("%.2f" % nbytes).rstrip("0").rstrip(".")
    return "%s %s" % (f, suffixes[i])


@login_required
@permission_required_or_403("view_project", (Project, "id", "project_id"))
def details(request, project_id):
    logger.debug("details")
    # Display the complete project page from his ID
    project = get_object_or_404(Project, pk=project_id)
    access = users.get_access_level(request, project_id)
    progress_bar, space_info_list_2 = progressbar(project, project)
    return render(
        request,
        "projects/details.html",
        {
            "project": project,
            "access": access,
            "space_info_list": space_info_list_2,
            "progress_bar": progress_bar,
        },
    )


@login_required
@permission_required_or_403("delete_project", (Project, "id", "project_id"))
def delete(request, *args, **kwargs):
    # Delete an openlink object
    project_id = kwargs["project_id"]
    project = get_object_or_404(Project, id=project_id)
    obj_id = kwargs["pk"]
    data_type = kwargs["data_type"]
    Model = apps.get_model("core", data_type.capitalize())
    obj_to_delete = get_object_or_404(Model, id=obj_id)
    if request.method == "POST":
        if data_type == "mapping":
            obj_to_delete = get_object_or_404(Mapping, id=obj_id)
            obj_to_delete.delete()

            messages.info(request, str(obj_to_delete) + " deleted")

            return HttpResponseRedirect(
                reverse("core:projects-details", kwargs={"project_id": project_id})
            )
        else:
            if data_type == "project":
                if not request.user.has_perm("manage_user", project):
                    return HttpResponseForbidden()
                else:
                    obj_to_delete.delete()
                    messages.info(request, str(obj_to_delete) + " deleted")
                    return HttpResponseRedirect(reverse("core:projects"))
            else:
                obj_to_delete.delete()
                messages.info(request, str(obj_to_delete) + " deleted")

        return HttpResponseRedirect(
            reverse("core:projects-details", kwargs={"project_id": project_id})
        )

    else:
        if data_type == "project":
            if not request.user.has_perm("manage_user", project):
                return HttpResponseForbidden()
            else:
                form = LinkProjectForm
        if data_type == "investigation":
            form = LinkInvestigationForm
        if data_type == "dataset":
            form = LinkDatasetForm
        if data_type == "assay":
            form = LinkAssayForm
        if data_type == "study":
            form = LinkStudyForm
        if data_type == "mapping":
            form = LinkMappingForm
    return render(
        request,
        "mapping/form_delete.html",
        {
            "form": form,
            "obj": obj_to_delete,
            "data_type": kwargs["data_type"],
            "project_id": project_id,
        },
    )


def progressbar(item, project):
    # Build progressbar of filesize
    space_info_list = []
    all_tools = []
    progress_bar = 0
    all_tools = Tool.objects.filter(project=project)
    obj = apps.get_model("core", str(item.type))
    all_datasets = obj.get_dataset(item.id)
    for tool in all_tools:
        if not issubclass(tool.get_connector(), Publisher):
            dataset_exists = False
            sum_space = 0
            for dataset in all_datasets:
                if Mapping.objects.filter(
                    foreign_id_obj__dataset=dataset, tool_id=tool
                ).exists():
                    dataset_exists = True
                    maps = Mapping.objects.filter(
                        foreign_id_obj__dataset=dataset, tool_id=tool
                    )
                    for mapping in maps:
                        size = mapping.size
                        if size is not None:
                            sum_space += size
            if dataset_exists is True:
                space_info_list.append(
                    {"size_total": sum_space, "tool_name": tool.name, "tool": tool}
                )
    sum_space = 0
    list_tool = []
    space_info_list_2 = []
    tool_name = ""
    tool = ""
    total_sum_space = 0
    for space in space_info_list:
        if space["tool_name"] not in list_tool:
            sum_space = space["size_total"]
            total_sum_space += sum_space
            tool_name = space["tool_name"]
            tool = space["tool"]
            space_info_list_2.append(
                {
                    "size_total": humansize(sum_space),
                    "tool_name": tool_name,
                    "tool": tool,
                }
            )
            list_tool.append(space["tool_name"])
        else:
            sum_space = sum_space + space["size_total"]
            for d in space_info_list_2:
                d.update(
                    ("size_total", humansize(sum_space))
                    for k, v in d.items()
                    if d["tool_name"] == tool_name
                )
    for value in space_info_list_2:
        if value["size_total"] != "0 B":
            percent_space = convert_to_byte(value["size_total"]) / total_sum_space * 100
            value["percent_space"] = percent_space
            progress_bar = 1
        else:
            value["percent_space"] = 0
    space_info_list_2.append(
        {"size_total": humansize(total_sum_space), "tool_name": "total", "tool": -1}
    )
    return progress_bar, space_info_list_2
