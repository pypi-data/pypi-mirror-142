import logging

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from openlink.core.forms import AddProjectUserForm
from openlink.core.models import MappingProjectUser, Project

logger = logging.getLogger(__name__)


@login_required
def get_access_level(request, project_id):
    # return current user access level for a given project
    access_level = ""
    user = request.user
    try:
        projects_list_user = Project.objects.get(
            author__user=request.user, id=project_id
        )
    except Project.DoesNotExist:
        projects_list_user = None
    if projects_list_user:
        access_level = str("administrator")
    proj_map = (
        MappingProjectUser.objects.filter(user__user=user)
        .filter(project__id=project_id)
        .values()
    )
    if proj_map.exists():
        for value in proj_map:
            access_level = value["role"]
    return access_level


@login_required
def add_user_mapping(request, *args, **kwargs):
    # Select a user to be map to the current project
    current_user = request.user
    current_proj = kwargs["project_id"]
    data_type = "project"
    mpu_list = MappingProjectUser.objects.filter(project__id=current_proj)
    project = get_object_or_404(Project, id=current_proj)

    if request.method == "POST":
        form = AddProjectUserForm(request.POST)
        user_mapping = form.save(commit=False)
        user_mapping.name = str(current_proj) + "_" + str(form.cleaned_data.get("user"))
        user_mapping.project = project
        user_mapping.save()
        messages.info(request, "User " + str(form.cleaned_data.get("user")) + " added")

        return HttpResponseRedirect(
            reverse("core:add_user_mapping", args=[current_proj])
        )

    else:
        form = AddProjectUserForm()

    return render(
        request,
        "mapping/add_user_mapping.html",
        {
            "form": form,
            "current_proj": current_proj,
            "data_type": data_type,
            "current_user": current_user,
            "data_type": data_type,
            "mpu_list": mpu_list,
            "project": project,
        },
    )
