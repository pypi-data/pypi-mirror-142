import json
import logging

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Button, Submit
from django.apps import apps
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
from django.views.decorators.http import require_POST
from django.views.generic.edit import UpdateView
from guardian.decorators import permission_required_or_403
from openlink.core.connector import Mapper, Publisher
from openlink.core.forms import (
    AssayForm,
    DatasetForm,
    InvestigationForm,
    ProjectForm,
    SelectAssayForm,
    SelectStudyForm,
    StudyForm,
)
from openlink.core.models import (
    Assay,
    Dataset,
    Investigation,
    Mapping,
    Profile,
    Project,
    Study,
    Tool,
)
from openlink.core.views import projects

logger = logging.getLogger(__name__)


def get_items_id(obj, list_save):
    # Get items structure
    if hasattr(obj, "items"):
        for item in obj.items:
            list_save.append(item)
            get_items_id(item, list_save)
        return list_save


@login_required
@permission_required_or_403("change_project", (Project, "id", "project_id"))
def add_investigation(request, project_id, **kwargs):
    # Display an empty form to add a new investigation

    project = get_object_or_404(Project, pk=project_id)
    if request.method == "GET":
        items = {}
        items["project"] = project
        return render(
            request,
            "new_item/new_item.html",
            {
                "form": InvestigationForm(),
                "project": project,
                "parent": project,
                "item": "investigation",
            },
        )
    elif request.method == "POST":
        form = InvestigationForm(request.POST)
        form.parent_id = project_id
        if not form.is_valid():
            # Display the same empty investigation form if form is not valid
            return render(
                request,
                "new_item/new_item.html",
                {
                    "form": form,
                    "project": project,
                    "parent": project,
                    "item": "investigation",
                },
            )
        profile = get_object_or_404(Profile, user=request.user)

        investigation = Investigation.create(
            form=form, profile=profile, parent_id=project_id
        )

        messages.info(request, "Investigation " + str(investigation.name) + " created")

        return HttpResponseRedirect(reverse("core:projects-details", args=[project_id]))


@login_required
@permission_required_or_403("change_project", (Project, "id", "project_id"))
def add_study(request, investigation_id, project_id):
    # Display an empty form to add a new study  in a given project ID
    investigation = get_object_or_404(Investigation, pk=investigation_id)
    project = get_object_or_404(Project, pk=project_id)
    if request.method == "GET":
        return render(
            request,
            "new_item/new_item.html",
            {
                "form": StudyForm(),
                "project": project,
                "investigation": investigation,
                "parent": investigation,
                "item": "study",
            },
        )
    elif request.method == "POST":
        form = StudyForm(request.POST)
        form.parent_id = investigation_id
        if not form.is_valid():
            # Display the same empty study form if form is not valid
            return render(
                request,
                "new_item/new_item.html",
                {
                    "form": form,
                    "project": project,
                    "investigation": investigation,
                    "parent": investigation,
                    "item": "study",
                },
            )

        profile = get_object_or_404(Profile, user=request.user)
        study = Study.create(form=form, profile=profile, parent_id=investigation_id)

        messages.info(request, "Study " + str(study.name) + " created")

        # Add the new study in the given investigation model instance

        return HttpResponseRedirect(reverse("core:projects-details", args=[project_id]))


@login_required
@permission_required_or_403("change_project", (Project, "id", "project_id"))
def select_study_to_create_assay(request, project_id, investigation_id):
    # Display a form in order to select a study, in which the user want to create a new assay
    if request.method == "POST":
        study_id = request.POST["studies_name"]
        project = get_object_or_404(Project, pk=project_id)
        investigation = get_object_or_404(Investigation, pk=investigation_id)
        study = get_object_or_404(Study, pk=study_id)
        return render(
            request,
            "new_item/new_item.html",
            {
                "form": AssayForm(),
                "study": study,
                "investigation": investigation,
                "project": project,
                "parent": study,
                "item": "assay",
            },
        )
    else:

        investigation = get_object_or_404(Investigation, pk=investigation_id)
        project = get_object_or_404(Project, pk=project_id)
        return render(
            request,
            "new_item/form_choose_study.html",
            {
                "form": SelectStudyForm(instance=investigation),
                "investigation": investigation,
                "project": project,
            },
        )


@login_required
@require_POST
@permission_required_or_403("change_project", (Project, "id", "project_id"))
def add_assay(request, project_id, investigation_id, study_id):
    # Save the new assay with data from the assay form
    form = AssayForm(request.POST)
    study = get_object_or_404(Study, id=study_id)
    form.parent_id = study_id
    if not form.is_valid():
        project = get_object_or_404(Project, pk=project_id)
        investigation = get_object_or_404(Investigation, pk=investigation_id)
        return render(
            request,
            "new_item/new_item.html",
            {
                "form": form,
                "study": study,
                "investigation": investigation,
                "project": project,
                "parent": study,
                "item": "assay",
            },
        )

    profile = get_object_or_404(Profile, user=request.user)
    assay = Assay.create(form, profile, study.id)

    messages.info(request, "Assay " + str(assay.name) + " created")

    return HttpResponseRedirect(reverse("core:projects-details", args=[project_id]))


@login_required
@permission_required_or_403("change_project", (Project, "id", "project_id"))
def select_assay_to_create_dataset(request, project_id, investigation_id):
    # Display a form in order to select a assay, in which the user want to create a new dataset
    if request.method == "POST":
        assay_id = request.POST["assays_name"]
        project = get_object_or_404(Project, pk=project_id)
        investigation = get_object_or_404(Investigation, pk=investigation_id)
        assay = get_object_or_404(Assay, pk=assay_id)
        return render(
            request,
            "new_item/new_item.html",
            {
                "form": DatasetForm(),
                "assay": assay,
                "investigation": investigation,
                "project": project,
                "parent": assay,
                "item": "dataset",
            },
        )
    else:

        project = get_object_or_404(Project, pk=project_id)
        investigation = get_object_or_404(Investigation, pk=investigation_id)
        return render(
            request,
            "new_item/form_choose_assay.html",
            {
                "form": SelectAssayForm(instance=investigation),
                "investigation": investigation,
                "project": project,
            },
        )


@login_required
@require_POST
@permission_required_or_403("change_project", (Project, "id", "project_id"))
def add_dataset(request, project_id, investigation_id, assay_id):
    # Save the new dataset with data from the dataset form
    form = DatasetForm(request.POST)
    assay = get_object_or_404(Assay, id=assay_id)
    form.parent_id = assay_id
    if not form.is_valid():
        project = get_object_or_404(Project, pk=project_id)
        investigation = get_object_or_404(Investigation, pk=investigation_id)
        return render(
            request,
            "new_item/new_item.html",
            {
                "form": form,
                "assay": assay,
                "investigation": investigation,
                "project": project,
                "parent": assay,
                "item": "dataset",
            },
        )

    profile = get_object_or_404(Profile, user=request.user)
    dataset = Dataset.create(form, profile, assay.id)

    messages.info(request, "Dataset " + str(dataset.name) + " created")

    return HttpResponseRedirect(reverse("core:projects-details", args=[project_id]))


@login_required
def get_json_object(request, *args, **kwargs):
    # Build json data to display from json connector
    tool_id = kwargs["tool_id"]
    object_id = kwargs["map_id"]
    data_type = kwargs["data_type"]
    json_data = []
    tool = get_object_or_404(Tool, id=tool_id)
    connector = tool.get_connector()
    elements_json = connector.get_dir(object_id)
    for element in elements_json:
        if data_type == "dataset":
            if element.__class__.__name__ == "DataObject":
                json_data.append(
                    {
                        "id": element.id,
                        "parent": object_id,
                        "text": element.name,
                        "icon": "jstree-file",
                    }
                )
            elif element.__class__.__name__ == "ContainerDataObject":
                json_data.append(
                    {
                        "id": element.id,
                        "parent": object_id,
                        "text": element.name,
                        "icon": "jstree-folder",
                    }
                )
        else:
            if element.__class__.__name__ == "DataObject":
                json_data.append(
                    {
                        "id": element.id,
                        "parent": object_id,
                        "text": element.name,
                        "icon": "jstree-file",
                        "state": {"checkbox_disabled": True},
                    }
                )
            elif element.__class__.__name__ == "ContainerDataObject":
                json_data.append(
                    {
                        "id": element.id,
                        "parent": object_id,
                        "text": element.name,
                    }
                )
    json_tree = json.dumps(json_data)

    return render(request, "tools/json_list.html", {"json_tree": json_tree})


def get_plural_form_of_type(type):
    plural_form = {
        "investigation": "investigations",
        "study": "studies",
        "assay": "assays",
        "dataset": "datasets",
    }
    return plural_form[type]


class ItemUpdate(UpdateView):
    # Generic class for item update
    template_name = "item_update/item_update_form.html"

    def __init__(self, *args, **kwargs):
        super(ItemUpdate, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_group_wrapper_class = "row"
        self.helper.label_class = "col-sm-offset-1 col-sm-2"
        self.helper.field_class = "col-md-8"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = self.object.name
        context["id"] = self.object.id
        context["data_type"] = str(self.object.type)
        obj = apps.get_model("core", str(self.object.type))
        investigation = obj.get_investigation(self.object.id).first()
        context["item"] = get_object_or_404(obj, id=self.object.id)
        if obj == Dataset:
            assay = get_object_or_404(Assay, datasets__id=self.object.id)
            context["assay_linked"] = Mapping.objects.filter(
                foreign_id_obj__assay__id=assay.id
            ).exists()
        if context["data_type"] != "project":
            project = obj.get_project(self.object.id).first()
            context["project"] = project
            context["investigation"] = investigation
            self.request.session["reference_data_type"] = self.object.type
            context["request"] = self.request
            context["progress_bar"], context["space_info_list"] = projects.progressbar(
                context["item"], project
            )
            items_mapping = Mapping.objects.filter(foreign_id_obj=context["item"])
            mappings = []
            for item_mapping in items_mapping:
                mapping = []
                connector = item_mapping.connector_class
                if issubclass(connector.__class__, Mapper):
                    supported_types = item_mapping.get_supported_types_plural
                else:
                    supported_types = []
                mapping.append(item_mapping)
                mapping.append(supported_types)
                mappings.append(mapping)
            context["mappings"] = mappings
            context["nb_mapper"] = 0
            context["nb_publisher"] = 0
            for value in items_mapping:
                if (
                    issubclass(
                        Tool.objects.get(id=value.tool_id.id).get_connector().__class__,
                        Publisher,
                    )
                    is True
                ):
                    context["nb_publisher"] += 1
                else:
                    context["nb_mapper"] += 1
            context["investigation_linked"] = Mapping.objects.filter(
                foreign_id_obj__investigation__id=context["investigation"].id
            ).exists()
            return context
        else:
            context["item"] = get_object_or_404(Project, id=self.object.id)
            return context

    def form_valid(self, form, *args, **kwargs):
        project_id = self.kwargs["project_id"]
        project = get_object_or_404(Project, id=project_id)
        if not self.request.user.has_perm("change_project", project):
            return HttpResponseForbidden()
        item = form.save(commit=False)
        item.date_modified = timezone.now()
        item.save()
        messages.info(
            self.request, item.type.capitalize() + " " + str(item.name) + " updated"
        )
        return HttpResponseRedirect(self.request.get_full_path())

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.helper = FormHelper()
        form.helper.form_group_wrapper_class = "row"
        form.helper.label_class = "col-sm-offset-1 col-sm-2"
        form.helper.field_class = "col-md-8"
        form.helper.add_input(
            Button(
                "back",
                "Back",
                css_class="btn-secondary",
                onClick="javascript:history.go(-1);",
            )
        )
        form.helper.add_input(
            Submit(
                "submit",
                "Update " + self.object.type.capitalize(),
                css_class="btn-primary",
            )
        )
        return form


class ProjectUpdate(ItemUpdate):
    # Generic editing view for a given Project
    model = Project
    form_class = ProjectForm
    template_name = "item_update/project_update_form.html"
    pk_url_kwarg = "project_id"


class InvestigationUpdate(ItemUpdate):
    # Generic editing view for a given Investigation
    model = Investigation
    form_class = InvestigationForm
    pk_url_kwarg = "investigation_id"


class StudyUpdate(ItemUpdate):
    # Generic editing view for a given study
    model = Study
    form_class = StudyForm
    pk_url_kwarg = "study_id"


class AssayUpdate(ItemUpdate):
    # Generic editing view for a given Experience
    model = Assay
    form_class = AssayForm
    pk_url_kwarg = "assay_id"


class DatasetUpdate(ItemUpdate):
    # Generic editing view for a given Dataset
    model = Dataset
    form_class = DatasetForm
    pk_url_kwarg = "dataset_id"
