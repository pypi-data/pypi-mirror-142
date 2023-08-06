import logging

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.apps import apps
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
from django.views.decorators.http import require_GET, require_POST
from django.views.generic.edit import UpdateView
from guardian.decorators import permission_required_or_403
from openlink.core import connector as tools
from openlink.core.connector import Mapper, Publisher
from openlink.core.forms import LinkToolForm, SelectToolForm, ToolForm, ToolProjectForm
from openlink.core.models import Mapping, Profile, Project, Tool, Toolparam

logger = logging.getLogger(__name__)


@login_required
@permission_required_or_403("change_project", (Project, "id", "project_id"))
def list_tools_project(request, project_id):
    # get list of tools linked to a project
    project = get_object_or_404(Project, id=project_id)
    list_tools_project = Tool.objects.filter(project__id=project_id)
    return render(
        request,
        "tools/list_tool_project.html",
        {"list_tools_project": list_tools_project, "project": project},
    )


@login_required
@require_GET
@permission_required_or_403("change_project", (Project, "id", "project_id"))
def select_connector_project(request, project_id):
    # Get selected connector and return the suited tool form
    project = get_object_or_404(Project, id=project_id)
    if "connector" not in request.GET:
        form = ToolForm()
        return render(
            request,
            "tools/new-choose-connector-project.html",
            {"form": form, "project": project},
        )
    else:
        form = ToolForm(request.GET)
        form.project_id = project_id
        if form.is_valid():
            connector_class = tools.get_connector_class(request.GET["connector"])
            tool_name = request.GET["name"]
            if connector_class is None:
                # TODO: add a message (https://docs.djangoproject.com/fr/3.0/ref/contrib/messages/#using-messages-in-views-and-templates)
                return HttpResponseRedirect(
                    reverse("core:add-tool-project", args=[project_id])
                )
            return render(
                request,
                "tools/add_tool_project.html",
                {
                    "form": connector_class.get_creation_form(),
                    "connector": connector_class.__name__,
                    "tool_name": tool_name,
                    "project": project,
                    "logo": connector_class.get_logo,
                },
            )
        else:
            messages.error(
                request, "unable to select " + request.GET["name"] + " tool connector"
            )
            return render(
                request,
                "tools/new-choose-connector-project.html",
                {"form": form, "project": project},
            )


@login_required
@require_POST
@permission_required_or_403("change_project", (Project, "id", "project_id"))
def add_tool_project(request, connector, project_id):
    # Display tool creation form  and create tool if the form is valid
    connector_class = tools.get_connector_class(connector)
    form = connector_class.get_creation_form(request.POST)
    project = get_object_or_404(Project, id=project_id)
    form.project_id = project_id
    try:
        if not form.is_valid():
            logger.debug(request.POST.get("name"))
            messages.error(
                request, "unable to add " + connector_class.get_name() + " tool"
            )
            return render(
                request,
                "tools/add_tool_project.html",
                {
                    "form": form,
                    "connector": connector,
                    "project": project,
                    "logo": connector_class.get_logo,
                    "tool_name": request.POST.get("name"),
                },
            )
    except Exception as e:
        messages.error(request, str(e))
        return render(
            request,
            "tools/add_tool_project.html",
            {
                "form": form,
                "connector": connector,
                "project": project,
                "logo": connector_class.get_logo,
                "tool_name": request.POST.get("name"),
            },
        )

    if form.is_valid():
        profile = Profile.objects.get(user=request.user)

        # Save new Tool using form entries
        logger.debug(request.POST)
        tool = Tool(
            name=request.POST.get("name"),
            connector=connector_class.__name__,
            author=profile,
            date_created=timezone.now(),
            project=project,
        )
        tool.save()
        for param in form.cleaned_data:
            url_param = Toolparam(
                tool_id=tool, key=param, value=form.cleaned_data[param]
            )
            url_param.save()
    # TODO: add a message (https://docs.djangoproject.com/fr/3.0/ref/contrib/messages/#using-messages-in-views-and-templates)
    return HttpResponseRedirect(reverse("core:tools-project", args=[project_id]))


@login_required
# @require_POST
@permission_required_or_403("change_project", (Project, "id", "project_id"))
def toolsparam_edit_project(request, *args, **kwargs):
    # Update tool parameters
    tool = get_object_or_404(Tool, pk=kwargs["tool_id"])
    project = get_object_or_404(Project, pk=kwargs["project_id"])
    connector = tool.connector
    connector_class = tools.get_connector_class(connector)
    if request.method == "POST":
        form = connector_class.get_edition_form(request.POST)
        toolsparam = get_object_or_404(Toolparam, tool_id=kwargs["tool_id"], key="url")
        form.set_url(toolsparam.value)
        if not form.is_valid():
            messages.error(
                request, "unable to add " + connector_class.get_name() + " tool"
            )
            return render(
                request,
                "tools/edit_toolparam_project.html",
                {
                    "form": form,
                    "connector": connector_class.get_name(),
                    "project": project,
                    "tool": tool,
                    "logo": connector_class.get_logo,
                },
            )
        if form.is_valid():
            for param in form.cleaned_data:
                instance_param = Toolparam.objects.get(tool_id=tool, key=param)
                instance_param.value = form.cleaned_data[param]
                instance_param.save()

        # TODO: add a message (https://docs.djangoproject.com/fr/3.0/ref/contrib/messages/#using-messages-in-views-and-templates)
        messages.info(request, "Tool parameters updated")
        return HttpResponseRedirect(reverse("core:tools-project", args=[project.id]))
    else:
        form = connector_class.get_edition_form()
        return render(
            request,
            "tools/edit_toolparam_project.html",
            {
                "form": form,
                "connector": connector_class.get_name(),
                "project": project,
                "tool": tool,
                "logo": connector_class.get_logo,
            },
        )


@login_required
@permission_required_or_403("change_project", (Project, "id", "project_id"))
def get_tool_info_project(request, *args, **kwargs):
    # get tool details for a given OpenLink poject
    project = get_object_or_404(Project, id=kwargs["project_id"])
    t_list = Tool.objects.filter(pk=kwargs["tool_id"])
    context = {"tool_list": t_list, "project": project}
    return render(request, "tools/tool_info_project.html", context)


class ToolUpdate(UpdateView):
    # Generic editing view for a given Experience
    model = Tool
    form_class = ToolProjectForm
    template_name = "tools/tool_update_form.html"
    pk_url_kwarg = "tool_id"

    def __init__(self, *args, **kwargs):
        super(ToolUpdate, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_group_wrapper_class = "row"
        self.helper.label_class = "col-sm-offset-1 col-sm-2"
        self.helper.field_class = "col-md-8"

    def get_context_data(self, **kwargs):
        project_id = self.kwargs["project_id"]
        context = super().get_context_data(**kwargs)
        context["name"] = self.object.name
        context["id"] = self.object.id
        context["tool"] = self.object
        project = get_object_or_404(Project, id=project_id)
        context["project"] = project
        return context

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.helper = FormHelper()
        form.helper.form_group_wrapper_class = "row"
        form.helper.label_class = "col-sm-offset-1 col-sm-2"
        form.helper.field_class = "col-md-8"
        form.helper.add_input(Submit("submit", "Update", css_class="btn-primary"))
        return form

    def dispatch(self, request, *args, **kwargs):
        return super(ToolUpdate, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        project_id = self.kwargs["project_id"]
        tool_id = self.kwargs["tool_id"]
        project = get_object_or_404(Project, id=project_id)
        if not self.request.user.has_perm("change_project", project):
            return HttpResponseForbidden()
        if form.is_valid():
            tool = form.save(commit=False)
            tool.save()
            messages.info(self.request, "Tool " + str(tool.name) + " saved")
            return HttpResponseRedirect(
                reverse("core:tools-project", args=[project.id])
            )
        else:
            return HttpResponseRedirect(
                reverse("core:tools-edit-project", args=[project_id, tool_id])
            )


@login_required
@permission_required_or_403("change_project", (Project, "id", "project_id"))
def delete_tool(request, *args, **kwargs):
    # delete selected tool
    obj_id = kwargs["pk"]
    project_id = kwargs["project_id"]
    data_type = "tool"
    Model = apps.get_model("core", data_type.capitalize())
    if Model.objects.filter(author__user=request.user, id=obj_id).exists():
        obj_to_delete = Model.objects.filter(author__user=request.user).get(id=obj_id)

    if request.method == "POST":
        obj_to_delete.delete()
        return HttpResponseRedirect(
            reverse("core:tools-project", kwargs={"project_id": project_id})
        )

    else:
        if data_type == "tool":
            form = LinkToolForm
    return render(
        request,
        "mapping/form_delete.html",
        {"form": form, "obj": obj_to_delete, "data_type": data_type},
    )


@login_required
@permission_required_or_403("change_project", (Project, "id", "project_id"))
def choose_tool(request, *args, **kwargs):
    # select a tool for the mapping of an OpenLink object
    tool_list = []
    if "investigation_id" in kwargs:
        current_inv = kwargs["investigation_id"]
        data_type = kwargs["data_type"]
    else:
        data_type = "investigation"
    current_proj = kwargs["project_id"]
    project = get_object_or_404(Project, id=current_proj)
    exist_tool = 0
    project_tools = Tool.objects.filter(project=project)
    pk = kwargs["pk"]
    for p in project_tools:
        exist_tool = 1
        connector = p.get_connector()
        if issubclass(connector.__class__, Mapper):
            list_ressource = connector.get_supported_types()
            if data_type in list_ressource:
                if data_type == "investigation":
                    try:
                        mo_list = Mapping.objects.get(
                            foreign_id_obj__investigation__id=pk, tool_id=p
                        )
                    except Mapping.DoesNotExist:
                        mo_list = None
                if data_type == "study":
                    try:
                        mo_list = Mapping.objects.get(
                            foreign_id_obj__study__id=pk, tool_id=p
                        )
                    except Mapping.DoesNotExist:
                        mo_list = None
                elif data_type == "assay":
                    try:
                        mo_list = Mapping.objects.get(
                            foreign_id_obj__assay__id=pk, tool_id=p
                        )
                    except Mapping.DoesNotExist:
                        mo_list = None
                elif data_type == "dataset":
                    try:
                        mo_list = Mapping.objects.get(
                            foreign_id_obj__dataset__id=pk, tool_id=p
                        )
                    except Mapping.DoesNotExist:
                        mo_list = None
                if mo_list is None:
                    tool_list.append(p)

    if request.method == "POST":
        host = request.POST["object_name"]
        result = Tool.objects.filter(id=int(host))

        for dp in result:
            tool_id = int(dp.id)
            # tag_tool = dp.tag_tool

            # kwargs['tool'] = str(dp['tool'])
        if "investigation_id" in kwargs:
            return HttpResponseRedirect(
                reverse(
                    "core:choose_non_linked_object_tool",
                    kwargs={
                        "project_id": kwargs["project_id"],
                        "investigation_id": current_inv,
                        "data_type": data_type,
                        "pk": kwargs["pk"],
                        "tool_id": tool_id,
                    },
                )
            )
        else:
            return HttpResponseRedirect(
                reverse(
                    "core:choose_non_linked_object_tool",
                    kwargs={
                        "project_id": kwargs["project_id"],
                        "data_type": data_type,
                        "pk": kwargs["pk"],
                        "tool_id": tool_id,
                    },
                )
            )

    else:
        form = SelectToolForm(instance=tool_list)

    if "investigation_id" in kwargs:
        return render(
            request,
            "tools/form_choose_tool.html",
            {
                "form": form,
                "project": project,
                "exist_tool": exist_tool,
                "tool_list": tool_list,
                "current_inv": current_inv,
                "data_type": data_type,
                "pk": pk,
                "tool_list": tool_list,
            },
        )
    else:
        return render(
            request,
            "tools/form_choose_tool.html",
            {
                "form": form,
                "project": project,
                "exist_tool": exist_tool,
                "tool_list": tool_list,
                "data_type": data_type,
                "pk": pk,
                "tool_list": tool_list,
            },
        )


@login_required
@permission_required_or_403("change_project", (Project, "id", "project_id"))
def choose_tool_for_publish(request, *args, **kwargs):
    # Select a tool where to publish data
    tool_list = []
    data_type = "investigation"
    current_proj = kwargs["project_id"]
    project = get_object_or_404(Project, id=current_proj)
    project_tools = Tool.objects.filter(project=project)
    pk = kwargs["pk"]

    for p in project_tools:
        connector = p.get_connector()
        if issubclass(connector.__class__, Publisher):
            tool_list.append(p)

    if request.method == "POST":
        host = request.POST["object_name"]
        result = Tool.objects.filter(id=int(host))
        for dp in result:
            tool_id = int(dp.id)
            tag_tool = dp.tag_tool
        return HttpResponseRedirect(
            reverse(
                "core:choose_object_to_publish",
                kwargs={
                    "project_id": kwargs["project_id"],
                    "data_type": data_type,
                    "pk": kwargs["pk"],
                    "tool": tag_tool,
                    "tool_id": tool_id,
                },
            )
        )

    else:
        form = SelectToolForm(instance=tool_list)
        return render(
            request,
            "tools/form_choose_tool.html",
            {
                "form": form,
                "project": project,
                "data_type": data_type,
                "pk": pk,
                "tool_list": tool_list,
                "function": "publish",
            },
        )
