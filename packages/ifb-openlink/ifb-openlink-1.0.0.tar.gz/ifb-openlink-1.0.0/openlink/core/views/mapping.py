import json
import logging
import urllib

import openlink.core.connector
from django.apps import apps
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
from guardian.decorators import permission_required_or_403
from guardian.shortcuts import assign_perm, remove_perm
from openlink.core.connector import ContainerDataObject, ContainerObject, Publisher
from openlink.core.forms import (
    LinkMappingForm,
    LinkMappingUserForm,
    SelectAssaysForm,
    SelectAssaysTool,
    SelectDatasetsTool,
    SelectMultipleObjectOption,
    SelectObjectOption,
    SelectObjectTool,
    SelectStudiesForm,
    SelectStudiesTool,
)
from openlink.core.lib import utils
from openlink.core.models import (
    Assay,
    Investigation,
    Mapping,
    MappingProjectUser,
    Profile,
    Project,
    Study,
    Tool,
)
from openlink.core.views import items

logger = logging.getLogger(__name__)


@login_required
@permission_required_or_403("change_project", (Project, "id", "project_id"))
def studies(request, *args, **kwargs):
    # Manage on-the-fly studies mapping
    # reference_data_type = request.session["reference_data_type"]
    project_id = kwargs["project_id"]
    investigation_id = kwargs["investigation_id"]
    tool_id = kwargs["tool_id"]
    tool = get_object_or_404(Tool, id=tool_id)
    map_id = kwargs["map_id"]
    data_type = "study"
    unlink_studies = []
    project = get_object_or_404(Project, author__user=request.user, pk=project_id)
    investigation = get_object_or_404(
        Investigation, author__user=request.user, pk=investigation_id
    )
    tools_qs = Tool.objects.filter(
        project=project,
        mapping__foreign_id_obj__investigation__id=investigation_id,
        mapping__object_id=map_id,
    )
    map_instance = Mapping.objects.get(
        foreign_id_obj__investigation__id=investigation_id, object_id=map_id
    )
    # Search for studies not linked to the current Openlink investigation
    for tool_qs in tools_qs:
        ms_list = Mapping.objects.filter(
            foreign_id_obj__study__investigation__id=investigation_id, tool_id=tool_qs
        )
        linked_studies = []
        for mapped_studies in ms_list:
            linked_studies.append(str(mapped_studies.object_id))
        connector = tool_qs.get_connector()
        reference_mapping = None
        container_mapping = ContainerObject(
            map_id, map_instance.name, map_instance.type
        )
        connector_studies = connector.get_data_objects(
            data_type, reference_mapping, container_mapping
        )
        for connector_study in connector_studies:
            if str(connector_study.id) not in linked_studies:
                unlink_studies.append(connector_study)

    studies = []
    if unlink_studies is not None:
        for study in unlink_studies:
            study = (str(study.id), study.name)
            studies.append(study)

    if request.method == "POST":
        list_studies = request.POST.getlist("study_name")
        objects_id = "%s" % (",".join(map(str, list_studies)))
        if len(list_studies) == 0:
            messages.info(request, "Please select at least one project!")
            form = SelectStudiesTool(studies)
            pass
        else:
            request.session["map_children"] = True
            request.session["data_type"] = data_type
            request.session["map_id"] = objects_id
            request.session["parent_id"] = investigation.id
            request.session["parent_type"] = "investigation"
            request.session["reference_data_type"] = "investigation"
            request.session["reference_data_id"] = investigation.id
            return HttpResponseRedirect(
                reverse(
                    "core:choose_option_mapping",
                    args=[project.id, investigation_id, data_type, tool.id, map_id],
                )
            )
    else:
        form = SelectStudiesTool(studies)
    return render(
        request,
        "mapping/item_list/studies_list.html",
        {
            "form": form,
            "project": project,
            "investigation": investigation,
            "unlink_studies": unlink_studies,
        },
    )


@login_required
@permission_required_or_403("change_project", (Project, "id", "project_id"))
def assays(request, *args, **kwargs):
    # Manage on-the-fly assays mapping
    # reference_data_type = request.session["reference_data_type"]
    project_id = kwargs["project_id"]
    investigation_id = kwargs["investigation_id"]
    map_id = kwargs["map_id"]
    unlink_assays = []
    data_type = "assay"
    structure = "list"
    json_tree = []
    project = get_object_or_404(Project, pk=project_id)
    investigation = get_object_or_404(Investigation, pk=investigation_id)
    if "study_id" in kwargs:
        tools_qs = Tool.objects.filter(
            mapping__foreign_id_obj__study__investigation__id=investigation_id,
            mapping__object_id=map_id,
        )
    else:
        tools_qs = Tool.objects.filter(
            mapping__foreign_id_obj__investigation__id=investigation_id,
            mapping__object_id=map_id,
        )
    # Search for assays not linked to the current Openlink investigation
    for tool_qs in tools_qs:
        ma_list = Mapping.objects.filter(
            foreign_id_obj__assay__study__investigation__id=investigation_id,
            tool_id=tool_qs,
        )
        linked_assays = []
        for mapped_assays in ma_list:
            linked_assays.append(str(mapped_assays.object_id))
        if "study_id" in kwargs:
            reference_mapping = Mapping.objects.get(
                foreign_id_obj__investigation__id=investigation_id, tool_id=tool_qs
            )
            container_mapping = Mapping.objects.get(
                foreign_id_obj__study__investigation__id=investigation_id,
                object_id=map_id,
                tool_id=tool_qs,
            )
            container_instance = ContainerObject(
                container_mapping.object_id,
                container_mapping.name,
                container_mapping.type,
            )
        else:
            reference_mapping = Mapping.objects.get(
                foreign_id_obj__investigation__id=investigation_id,
                object_id=map_id,
                tool_id=tool_qs,
            )
            container_instance = None
        reference_instance = ContainerObject(
            reference_mapping.object_id, reference_mapping.name, reference_mapping.type
        )
        connector = tool_qs.get_connector()
        connector_assays = connector.get_data_objects(
            "assay", reference_instance, container_instance
        )
        if connector.get_data_structure() == openlink.core.connector.TREE_STRUCTURE:
            structure = "tree"
            # Initiate tree structure
            investigation_info = connector.get_investigation(map_id)
            json_tree.append(
                {
                    "id": investigation_info.id,
                    "parent": "#",
                    "text": investigation_info.name,
                    "icon": "fa fa-inbox",
                    "state": {"checkbox_disabled": True},
                }
            )
        for connector_assay in connector_assays:
            if str(connector_assay.id) not in linked_assays:
                unlink_assays.append(connector_assay)
        tool = tool_qs
    assays = []
    if unlink_assays is not None:
        for assay in unlink_assays:
            assay = (str(assay.id), assay.name)
            assays.append(assay)
    # Create and link assays in selected study
    if request.method == "POST":
        list_assays = request.POST.getlist("assay_name")
        str_list_assays = ", ".join(list_assays)

        if "study_id" in kwargs:
            if len(list_assays) == 0:
                messages.info(request, "Please select at least one assay!")
                form = SelectAssaysTool(assays)
                pass
            else:
                request.session["map_children"] = True
                request.session["data_type"] = data_type
                request.session["map_id"] = str_list_assays
                request.session["parent_id"] = kwargs["study_id"]
                request.session["parent_type"] = "study"
                request.session["reference_data_type"] = "study"
                request.session["reference_data_id"] = kwargs["study_id"]
                return HttpResponseRedirect(
                    reverse(
                        "core:choose_option_mapping",
                        args=[
                            project.id,
                            investigation_id,
                            data_type,
                            kwargs["study_id"],
                            tool.id,
                            map_id,
                        ],
                    )
                )
        else:
            # Display a form to select a study where assays will be created
            form = SelectStudiesForm(investigation=investigation)
            if Study.objects.filter(investigation__id=investigation_id).exists():
                objects_to_select = True
            else:
                objects_to_select = False

            request.session["map_id"] = str_list_assays
            request.session["reference_data_type"] = "investigation"
            request.session["reference_data_id"] = investigation_id

            return render(
                request,
                "mapping/form_select_item.html",
                {
                    "form": form,
                    "project": project,
                    "investigation": investigation,
                    "selected_items": str_list_assays,
                    "map_id": map_id,
                    "type_to_select": "study",
                    "data_type": "assay",
                    "tool_id": tool.id,
                    "tool_name": connector.get_name,
                    "function": "select_assay_mapping",
                    "objects_to_select": objects_to_select,
                },
            )
    else:
        form = SelectAssaysTool(assays)

        if structure == "list":
            return render(
                request,
                "mapping/item_list/assays_list.html",
                {
                    "form": form,
                    "project": project,
                    "investigation": investigation,
                    "unlink_assay": unlink_assays,
                },
            )
        else:
            json_tree = json.dumps(json_tree)
            return render(
                request,
                "mapping/item_list/datasets_list.html",
                {
                    "form": form,
                    "project": project,
                    "investigation": investigation,
                    "id": project.id,
                    "json_tree": json_tree,
                    "data_type": "assay",
                    "structure": structure,
                    "tool": tool,
                },
            )


@login_required
@permission_required_or_403("change_project", (Project, "id", "project_id"))
def select_assay_mapping(request, *args, **kwargs):
    # Display study from the complete project page
    project_id = kwargs["project_id"]
    investigation_id = kwargs["investigation_id"]
    map_id = kwargs["map_id"]
    project = get_object_or_404(Project, pk=project_id)
    data_type = "assay"
    tools_qs = Tool.objects.filter(
        project=project,
        mapping__foreign_id_obj__investigation__id=investigation_id,
        mapping__object_id=map_id,
    )
    tool = tools_qs[0]

    if request.method == "POST":
        selected_study = request.POST.get("studies_name")
        selected_assays_string = request.POST.get("assay")
        map_id = str(selected_assays_string).strip("'<>() ").replace("'", '"')

        request.session["data_type"] = data_type
        request.session["map_id"] = selected_assays_string
        request.session["parent_id"] = selected_study
        request.session["map_children"] = True
        return HttpResponseRedirect(
            reverse(
                "core:choose_option_mapping",
                args=[project.id, investigation_id, data_type, tool.id, map_id],
            )
        )


@login_required
@permission_required_or_403("change_project", (Project, "id", "project_id"))
def datasets(request, *args, **kwargs):
    # reference_data_type = request.session["reference_data_type"]
    # Manage on-the-fly datasets mapping
    project_id = kwargs["project_id"]
    investigation_id = kwargs["investigation_id"]
    project = get_object_or_404(Project, pk=project_id)
    investigation = get_object_or_404(Investigation, pk=investigation_id)
    map_id = kwargs["map_id"]
    linked_datasets = []
    unlink_datasets = []
    data_type = "dataset"
    structure = "list"
    json_tree = []
    tool = Tool.objects.filter(project=project, mapping__object_id=map_id).first()
    connector = tool.get_connector()
    # Search for datasets not linked to the current Openlink investigation
    if "assay_id" in kwargs:
        if tool is None:
            map_id = urllib.parse.quote(map_id)
            tool = Tool.objects.filter(
                project=project, mapping__object_id=map_id
            ).first()
        assay_id = kwargs["assay_id"]
        assay = get_object_or_404(Assay, id=assay_id)
        mapping_assay = Mapping.objects.filter(
            foreign_id_obj__assay__id=assay.id, tool_id__connector=tool.connector
        )
        for map_assay in mapping_assay:
            map_assay_object = ContainerDataObject(
                map_assay.object_id, map_assay.name, map_assay.type
            )
            objects = connector.get_data_objects(data_type, None, map_assay_object)
            if connector.get_data_structure() == openlink.core.connector.TREE_STRUCTURE:
                structure = "tree"
                assay_info = connector.get_data_object("assay", map_assay.object_id)
                json_tree.append(
                    {
                        "id": assay_info.id,
                        "parent": "#",
                        "text": assay_info.name,
                        "state": {"checkbox_disabled": True},
                    }
                )
        mo_list = Mapping.objects.filter(
            foreign_id_obj__dataset__assay__id=assay.id,
            tool_id__connector=tool.connector,
        )
        for mapping_object in mo_list:
            linked_datasets.append((str(mapping_object.object_id)))
        for connector_object in objects:
            if str(connector_object.id) not in linked_datasets:
                if connector_object not in unlink_datasets:
                    unlink_datasets.append(connector_object)
        datasets = []
        if unlink_datasets is not None:
            for dataset in unlink_datasets:
                dataset = (str(dataset.id), dataset.name)
                datasets.append(dataset)
    elif "study_id" in kwargs:
        if tool is None:
            map_id = urllib.parse.quote(map_id)
            tool = Tool.objects.filter(
                project=project, mapping__object_id=map_id
            ).first()
        study_id = kwargs["study_id"]
        study = get_object_or_404(Study, id=study_id)
        mapping_study = Mapping.objects.filter(
            foreign_id_obj__assay__study__id=study.id, tool_id__connector=tool.connector
        )
        for map_study in mapping_study:
            map_study_object = ContainerDataObject(
                map_study.object_id, map_study.name, map_study.type
            )
            objects = connector.get_data_objects(data_type, None, map_study_object)
            if connector.get_data_structure() == openlink.core.connector.TREE_STRUCTURE:
                structure = "tree"
                study_info = connector.get_data_object("study", map_study.object_id)
                json_tree.append(
                    {
                        "id": study_info.id,
                        "parent": "#",
                        "text": study_info.name,
                        "state": {"checkbox_disabled": True},
                    }
                )
        mo_list = Mapping.objects.filter(
            foreign_id_obj__dataset__assay__study__id=study.id,
            tool_id__connector=tool.connector,
        )
        for mapping_object in mo_list:
            linked_datasets.append((str(mapping_object.object_id)))
        for connector_object in objects:
            if str(connector_object.id) not in linked_datasets:
                if connector_object not in unlink_datasets:
                    unlink_datasets.append(connector_object)
        datasets = []
        if unlink_datasets is not None:
            for dataset in unlink_datasets:
                dataset = (str(dataset.id), dataset.name)
                datasets.append(dataset)
    else:
        tools_qs = Tool.objects.filter(
            project=project,
            mapping__foreign_id_obj__investigation__id=investigation_id,
            mapping__object_id=map_id,
        )
        for tool_qs in tools_qs:
            md_list = Mapping.objects.filter(
                foreign_id_obj__dataset__assay__study__investigation__id=investigation_id,
                tool_id=tool_qs,
            )
            linked_datasets = []
            for mapped_datasets in md_list:
                linked_datasets.append(str(mapped_datasets.object_id))
            connector = tool_qs.get_connector()
            connector_datasets = connector.get_datasets(map_id)
            for connector_dataset in connector_datasets:
                if str(connector_dataset.id) not in linked_datasets:
                    unlink_datasets.append(connector_dataset)
        datasets = []
        if unlink_datasets is not None:
            for dataset in unlink_datasets:
                obj_id = dataset.id
                obj = dataset.name
                dataset = (str(obj_id), obj)
                datasets.append(dataset)
        if connector.get_data_structure() == openlink.core.connector.TREE_STRUCTURE:
            structure = "tree"
            investigation_info = connector.get_investigation(map_id)
            json_tree.append(
                {
                    "id": investigation_info.id,
                    "parent": "#",
                    "text": investigation_info.name,
                    "icon": "fa fa-inbox",
                    "state": {"checkbox_disabled": True},
                }
            )
    # Create and link datasets in selected assay
    if request.method == "POST":
        list_datasets = request.POST.getlist("dataset_name")
        str_list_datasets = (
            str(list_datasets)
            .strip("'<>() ")
            .replace("'", '"')
            .replace('["[', "[")
            .replace(']"]', "]")
        )
        selected_datasets = json.loads(str_list_datasets)
        str_list_datasets_final = ", ".join(selected_datasets)
        # If assay is already known
        if "assay_id" in kwargs:
            # selected_datasets = json.loads(dataform)
            # selected_assay = assay_id
            if len(list_datasets) == 0:
                messages.info(request, "Please select at least one dataset!")
                form = SelectDatasetsTool(datasets)
                pass
            else:
                request.session["map_children"] = True
                request.session["data_type"] = data_type
                request.session["map_id"] = str_list_datasets_final
                request.session["parent_id"] = kwargs["assay_id"]
                request.session["parent_type"] = "assay"
                request.session["reference_data_type"] = "assay"
                request.session["reference_data_id"] = kwargs["assay_id"]
                return HttpResponseRedirect(
                    reverse(
                        "core:choose_option_mapping",
                        args=[project.id, investigation_id, data_type, tool.id, map_id],
                    )
                )
        else:
            request.session["map_id"] = str_list_datasets_final
            if "study_id" in kwargs:
                request.session["reference_data_type"] = "study"
                request.session["reference_data_id"] = kwargs["study_id"]
            else:
                request.session["reference_data_type"] = "investigation"
                request.session["reference_data_id"] = kwargs["investigation_id"]
            if len(list_datasets) == 0:
                messages.info(request, "Please select at least one dataset!")
                form = SelectDatasetsTool(datasets)
                pass
            else:
                # Display a form to select a study where assays will be created
                form = SelectAssaysForm(investigation=investigation)
                if Assay.objects.filter(
                    study__investigation__id=investigation_id
                ).exists():
                    objects_to_select = True
                else:
                    objects_to_select = False
                return render(
                    request,
                    "mapping/form_select_item.html",
                    {
                        "form": form,
                        "project": project,
                        "investigation": investigation,
                        "selected_items": list_datasets,
                        "map_id": map_id,
                        "type_to_select": "assay",
                        "data_type": "dataset",
                        "connector": connector,
                        "function": "select_dataset_mapping",
                        "objects_to_select": objects_to_select,
                    },
                )

    else:
        form = SelectDatasetsTool(datasets)
    json_tree = json.dumps(json_tree)
    return render(
        request,
        "mapping/item_list/datasets_list.html",
        {
            "form": form,
            "project": project,
            "investigation": investigation,
            "unlink_datasets": unlink_datasets,
            "id": project.id,
            "json_tree": json_tree,
            "data_type": data_type,
            "structure": structure,
            "tool": tool,
        },
    )


@login_required
@permission_required_or_403("change_project", (Project, "id", "project_id"))
def select_dataset_mapping(request, *args, **kwargs):
    # Display studies and assay as in the complete project page
    project_id = kwargs["project_id"]
    investigation_id = kwargs["investigation_id"]
    map_id = kwargs["map_id"]
    project = get_object_or_404(Project, pk=project_id)
    tools_qs = Tool.objects.filter(
        project=project,
        mapping__foreign_id_obj__investigation__id=investigation_id,
        mapping__object_id=map_id,
    )
    tool = tools_qs[0]

    if request.method == "POST":
        selected_assay = request.POST.get("assays_name")
        selected_datasets_string = request.POST.get("dataset")
        dataform = str(selected_datasets_string).strip("'<>() ").replace("'", '"')
        selected_datasets = json.loads(dataform)

        request.session["data_type"] = "dataset"
        request.session["map_id"] = selected_datasets
        request.session["parent_id"] = selected_assay
        request.session["map_children"] = True
        return HttpResponseRedirect(
            reverse(
                "core:choose_option_mapping",
                args=[project.id, investigation_id, "dataset", tool.id, map_id],
            )
        )


def get_objects_linked_in_project(data_type, reference_project, tool):
    # Get a list of objects id already linked to an Openlink project
    linked_objects = []
    if data_type == "study":
        mo_list = Mapping.objects.filter(
            foreign_id_obj__study__investigation__project__id=reference_project,
            tool_id=tool,
        )
    elif data_type == "assay":
        mo_list = Mapping.objects.filter(
            foreign_id_obj__assay__study__investigation__project__id=reference_project,
            tool_id=tool,
        )
    elif data_type == "dataset":
        mo_list = Mapping.objects.filter(
            foreign_id_obj__dataset__assay__study__investigation__project__id=reference_project,
            tool_id=tool,
        )
    else:
        if data_type == "investigation":
            mo_list = Mapping.objects.filter(
                foreign_id_obj__investigation__project__id=reference_project,
                tool_id=tool,
            )

    for mo in mo_list:
        linked_objects.append(mo.object_id)
    return linked_objects


def get_objects_linked_in_investigation(data_type, reference_investigation, tool):
    # Get a list of objects id already linked to an Openlink investigation
    linked_objects = []
    if data_type == "study":
        mo_list = Mapping.objects.filter(
            foreign_id_obj__study__investigation__id=reference_investigation,
            tool_id=tool,
        )
    elif data_type == "assay":
        mo_list = Mapping.objects.filter(
            foreign_id_obj__assay__study__investigation__id=reference_investigation,
            tool_id=tool,
        )
    elif data_type == "dataset":
        mo_list = Mapping.objects.filter(
            foreign_id_obj__dataset__assay__study__investigation__id=reference_investigation,
            tool_id=tool,
        )
    for mo in mo_list:
        linked_objects.append(mo.object_id)
    return linked_objects


@login_required
@permission_required_or_403("change_project", (Project, "id", "project_id"))
def choose_non_linked_object_tool(request, *args, **kwargs):
    # Display a selection of available objects to link
    project = get_object_or_404(Project, id=kwargs["project_id"])
    tool_qs = get_object_or_404(Tool, project=project, id=kwargs["tool_id"])
    if "investigation_id" in kwargs:
        current_inv = kwargs["investigation_id"]
        reference_item = get_object_or_404(
            Investigation, project=project, id=current_inv
        )
        if Mapping.objects.filter(
            foreign_id_obj=reference_item, tool_id=tool_qs
        ).exists():
            reference_mapping = Mapping.objects.get(
                foreign_id_obj=reference_item, tool_id=tool_qs
            )
            reference_container = ContainerDataObject(
                reference_mapping.object_id,
                reference_mapping.name,
                reference_mapping.type,
            )
        else:
            reference_container = None
    else:
        reference_container = None
    pk = kwargs["pk"]
    data_type = kwargs["data_type"]
    request.session["reference_data_type"] = data_type
    request.session["reference_data_id"] = pk
    tool_id = kwargs["tool_id"]
    unlinked_objects = []
    parent_objects = []
    json_tree = []
    connector = tool_qs.get_connector()
    list_ressource = connector.get_supported_types()
    Model = apps.get_model("core", data_type)
    for item in list_ressource:
        if item == data_type:
            data_type_map = list_ressource[item]

    # Get a list of objects already linked to Openlink
    if data_type in list_ressource:
        linked_objects = get_objects_linked_in_project(data_type, project.id, tool_qs)

    # Get non linked DataObject and initiate json for tree structure
    item_parent = Model.get_parent(pk)[0]
    if Mapping.objects.filter(foreign_id_obj=item_parent, tool_id=tool_qs).exists():
        mapping_parent = Mapping.objects.get(
            foreign_id_obj=item_parent, tool_id=tool_qs
        )
        container_parent = ContainerDataObject(
            mapping_parent.object_id, mapping_parent.name, mapping_parent.type
        )
    else:
        container_parent = None

    for connector_object in connector.get_data_objects(
        data_type, reference_container, container_parent
    ):
        if str(connector_object.id) not in linked_objects:
            unlinked_objects.append(connector_object)

    if connector.get_data_structure() == openlink.core.connector.TREE_STRUCTURE:
        structure = "tree"
        if container_parent is not None:
            data_type_parent = Model.get_parent_type()
            parent_info = connector.get_data_object(
                str(data_type_parent.__name__).lower(), container_parent.id
            )
            json_tree.append(
                {
                    "id": parent_info.id,
                    "parent": "#",
                    "text": parent_info.name,
                    "state": {"checkbox_disabled": True},
                }
            )
        else:
            parents_info = connector.get_data_objects(
                data_type, reference_container, container_parent
            )
            for parent_info in parents_info:
                json_tree.append(
                    {
                        "id": parent_info.id,
                        "parent": "#",
                        "text": parent_info.name,
                        "state": {"checkbox_disabled": True},
                    }
                )
    else:
        structure = "list"

    if request.method == "POST":
        object_id = request.POST["object_name"]
        request.session["map_children"] = False
        request.session["data_type"] = data_type
        request.session["map_id"] = object_id
        print(object_id)
        for obj in unlinked_objects:
            if str(obj.id) == str(object_id):
                tool = tool_qs
                tool_id = tool.id

        # return to edit study URL
        if "investigation_id" not in kwargs:
            current_inv = pk
        return HttpResponseRedirect(
            reverse(
                "core:choose_option_mapping",
                args=[project.id, current_inv, data_type, pk, tool_id, object_id],
            )
        )

    else:
        form = SelectObjectTool(unlinked_objects)

    if "investigation_id" in kwargs:
        json_tree = json.dumps(json_tree)
        return render(
            request,
            "mapping/form_choose_object_mapping.html",
            {
                "form": form,
                "unlinked_objects": unlinked_objects,
                "current_proj": project.id,
                "current_inv": current_inv,
                "data_type": data_type,
                "data_type_map": data_type_map,
                "pk": pk,
                "function": "choose_non_linked_object",
                "project": project,
                "structure": structure,
                "parent_objects": parent_objects,
                "json_tree": json_tree,
                "tool": tool_id,
                "tool_name": tool_qs.name,
            },
        )
    else:
        return render(
            request,
            "mapping/form_choose_object_mapping.html",
            {
                "form": form,
                "unlinked_objects": unlinked_objects,
                "current_proj": project.id,
                "data_type": data_type,
                "data_type_map": data_type_map,
                "pk": pk,
                "function": "choose_non_linked_object",
                "project": project,
                "structure": structure,
                "parent_objects": parent_objects,
                "tool_name": tool_qs.name,
            },
        )


@login_required
@permission_required_or_403("change_project", (Project, "id", "project_id"))
def choose_option_mapping(request, *args, **kwargs):
    # Manage one item mapping and his options

    data_type = request.session["data_type"]
    author = get_object_or_404(Profile, user=request.user)
    tool = get_object_or_404(Tool, id=kwargs["tool_id"])
    connector = tool.get_connector()
    Model = apps.get_model("core", data_type)
    current_proj = kwargs["project_id"]
    reference_data_type = request.session["reference_data_type"]
    reference_data_id = request.session["reference_data_id"]
    project = get_object_or_404(Project, id=current_proj)
    if request.session["map_children"] is True:
        objects_id = request.session["map_id"].split(",")
        pk = request.session["parent_id"]
    else:
        pk = kwargs["pk"]
        objects_id = kwargs["map_id"].split(",")
        object_info = connector.get_data_object(data_type, objects_id[0])
        openlink_object = get_object_or_404(Model, id=kwargs["pk"])
    if "investigation_id" in kwargs:
        current_inv = kwargs["investigation_id"]
    list_ressource = connector.get_supported_types()
    reference_mapping = None

    # Get list of mapping type in plural form
    (
        data_type_map,
        list_objects,
        list_objects_map,
    ) = get_list_mapping_type_of_available_children(
        list_ressource, data_type, connector
    )

    if request.method == "POST":
        for object_id in objects_id:
            object_info = connector.get_data_object(data_type, object_id)

            # Get or Create Openlink object if it doesn't already exist
            if request.session["map_children"] is True:
                update_object = Model.create_instance(object_info, author)
                update_object.save()
                messages.info(request, str(update_object.name) + " created ")
                openlink_object = update_object
                parent_id = request.session["parent_id"]
                parent_type = Model.get_parent_type()
                parent_object = get_object_or_404(parent_type, id=parent_id)
                parent_type.link_child_to_parent(parent_object, openlink_object)
            else:
                update_object = get_object_or_404(Model, id=pk)

            # Update Openlink study name
            if "replace_openlink_name" in request.POST:
                name = utils.add_number_at_end_if_name_exist(
                    object_info.name, update_object
                )
                update_object.name = name
                update_object.date_modified = timezone.now()
                update_object.save()
                messages.info(
                    request,
                    data_type.capitalize() + " " + str(update_object.name) + " updated",
                )

            logger.debug(request.POST)
            if "use_description" in request.POST:
                update_object.description = object_info.description
                update_object.date_modified = timezone.now()
                update_object.save()
                messages.info(
                    request,
                    data_type.capitalize()
                    + " "
                    + str(update_object.name)
                    + " description updated",
                )
            elif "add_description" in request.POST:
                update_object.description = (
                    update_object.description + "\n" + object_info.description
                )
                update_object.date_modified = timezone.now()
                update_object.save()
                messages.info(
                    request,
                    data_type.capitalize()
                    + " "
                    + str(update_object.name)
                    + " description updated",
                )

            # Create Mapping for the new openlink object
            new_mapping_object = Mapping.create_instance(
                openlink_object, object_info, tool, author
            )
            new_mapping_object.save()
            messages.info(
                request, "Mapping " + str(new_mapping_object.name) + " created "
            )

            if "create_and_link_children" in request.POST:
                new_container_object = connector.get_data_object(
                    new_mapping_object.type, new_mapping_object.object_id
                )
                utils.create_children_mappings(
                    request,
                    tool,
                    openlink_object,
                    reference_mapping,
                    new_container_object,
                    author,
                )

            tool_option = {}
            for key, value in request.POST.items():
                if key.startswith(tool.name.lower()):
                    tool_option[key] = value
            if connector.has_mapping_options is True:
                connector.option_traitement(tool_option, new_mapping_object)
        # Return to edit openlink object page
        try:
            del request.session["parent_id"]
            del request.session["parent_type"]
            del request.session["reference_data_type"]
            del request.session["map_children"]
            del request.session["data_type"]
            del request.session["map_id"]
        except KeyError:
            pass
        if data_type == "investigation":
            return HttpResponseRedirect(
                reverse(
                    "core:edit-" + str(data_type),
                    args=[current_proj, kwargs["pk"]],
                )
            )
        else:
            if "reference_data_id" in request.session:
                del request.session["reference_data_id"]
                if current_inv == reference_data_id:
                    return HttpResponseRedirect(
                        reverse(
                            "core:edit-" + str(reference_data_type),
                            args=[current_proj, reference_data_id],
                        )
                    )
                else:
                    return HttpResponseRedirect(
                        reverse(
                            "core:edit-" + str(reference_data_type),
                            args=[current_proj, current_inv, reference_data_id],
                        )
                    )
            else:
                return HttpResponseRedirect(
                    reverse(
                        "core:edit-" + str(data_type),
                        args=[current_proj, current_inv, kwargs["pk"]],
                    )
                )

    else:
        has_mapping_options = tool.get_connector().has_mapping_options()
        if request.session["map_children"] is True:
            form = SelectMultipleObjectOption(
                data_type_map=data_type_map,
                has_mapping_options=has_mapping_options,
                tool_connector=connector,
                list_objects=list_objects,
                list_objects_map=list_objects_map,
                action="choose_option_mapping",
            )
            return render(
                request,
                "mapping/form_choose_option_mapping.html",
                {
                    "form": form,
                    "current_proj": current_proj,
                    "current_inv": current_inv,
                    "data_type": data_type,
                    "data_type_map": data_type_map,
                    "tool_name": tool.name,
                    "project": project,
                    "function": "choose_option_mapping",
                    "pk": pk,
                },
            )

        else:
            if "pk" in kwargs:
                form = SelectObjectOption(
                    data_type=data_type,
                    data_type_map=data_type_map,
                    object_name=object_info.name,
                    has_mapping_options=has_mapping_options,
                    tool_connector=connector,
                    object_desc=object_info.description,
                    list_objects=list_objects,
                    list_objects_map=list_objects_map,
                    action="choose_option_mapping",
                )
                return render(
                    request,
                    "mapping/form_choose_option_mapping.html",
                    {
                        "form": form,
                        "current_proj": current_proj,
                        "current_inv": current_inv,
                        "data_type": reference_data_type,
                        "pk": kwargs["pk"],
                        "data_type_map": data_type_map,
                        "tool_name": tool.name,
                        "project": project,
                        "object_desc": object_info.description,
                        "function": "choose_option_mapping",
                    },
                )


@login_required
@permission_required_or_403("change_project", (Project, "id", "project_id"))
def delete_mapping(request, *args, **kwargs):
    # Delete mapping instance from openlink
    project_id = kwargs["project_id"]
    investigation_id = kwargs["investigation_id"]
    obj_id = kwargs["pk"]
    data_type = kwargs["data_type"]
    obj_to_delete = get_object_or_404(Mapping, id=obj_id)
    logging.debug(obj_to_delete)
    type_to_delete = obj_to_delete.type
    type_id = obj_to_delete.foreign_id_obj.id
    if request.method == "POST":

        if data_type == "investigation":
            investigation = get_object_or_404(Investigation, id=investigation_id)
            tool_qs = get_object_or_404(Tool, mapping__id=obj_id)
            tool_id = tool_qs.id
            connector = tool_qs.get_connector()
            list_save = []
            list_items = items.get_items_id(investigation, list_save)
            object_id = get_object_or_404(Mapping, id=obj_id).object_id
            for item in list_items:
                try:
                    if issubclass(connector.__class__, Publisher):
                        mapping_query = Mapping.objects.get(
                            foreign_id_obj=item,
                            tool_id__id=tool_id,
                            object_id=object_id,
                        )
                    else:
                        mapping_query = Mapping.objects.get(
                            foreign_id_obj=item, tool_id__id=tool_id
                        )
                except Mapping.DoesNotExist:
                    mapping_query = None
                if mapping_query:
                    mapping_obj_to_delete = mapping_query
                    mapping_obj_to_delete.delete()
                    messages.info(request, str(mapping_obj_to_delete) + " deleted")

        obj_to_delete = get_object_or_404(Mapping, id=obj_id)
        logging.debug(obj_to_delete)
        obj_to_delete.delete()

        return HttpResponseRedirect(
            reverse(
                "core:edit-" + str(data_type),
                kwargs={
                    "project_id": project_id,
                    "investigation_id": investigation_id,
                    str(data_type) + "_id": type_id,
                },
            )
        )

    else:
        form = LinkMappingForm
    return render(
        request,
        "mapping/form_delete_mapping.html",
        {
            "form": form,
            "obj": obj_to_delete,
            "data_type": type_to_delete,
            "project_id": project_id,
            "investigation_id": investigation_id,
            "type_id": type_id,
        },
    )


def delete_user_mapping(request, *args, **kwargs):
    # Delete user and his mapping objects from a project
    project_id = kwargs["project_id"]
    project = get_object_or_404(Project, id=project_id)
    if request.method == "POST":
        users_to_delete = request.POST["users_list"]
        users_collection = users_to_delete.split(",")
        for user in users_collection:
            if user != "":
                user_to_delete = get_object_or_404(MappingProjectUser, id=user)
                username_to_delete = user_to_delete.user
                user_to_delete.delete()
                messages.info(
                    request, str(username_to_delete) + " deleted from " + str(project)
                )

                list_save = []
                list_items = items.get_items_id(project, list_save)
                for item in list_items:
                    try:
                        mapping_query = Mapping.objects.get(
                            foreign_id_obj=item, author=username_to_delete
                        )
                    except Mapping.DoesNotExist:
                        mapping_query = None
                    if mapping_query:
                        mapping_obj_to_delete = mapping_query
                        mapping_obj_to_delete.delete()
                        messages.info(request, str(mapping_obj_to_delete) + " deleted")

        return HttpResponseRedirect(
            reverse("core:mapping_project_user", args=[project_id])
        )


@login_required
@permission_required_or_403("manage_user", (Project, "id", "project_id"))
def mapping_project_user(request, *args, **kwargs):
    # Assign new user permissions to the current project
    current_user = request.user
    current_proj = kwargs["project_id"]
    data_type = "project"
    mpu_list = MappingProjectUser.objects.filter(project__id=current_proj)
    project = get_object_or_404(Project, id=current_proj)
    ManageProjectUserFormset = inlineformset_factory(
        Project,
        MappingProjectUser,
        fields=(
            "user",
            "role",
        ),
        extra=1,
        can_delete=True,
    )
    author = project.author
    list_delete_user = []

    delete_error = False
    author_exist = False
    author_admin_error = False
    if request.method == "POST":
        formset = ManageProjectUserFormset(request.POST, instance=project)
        if formset.is_valid():
            for form in formset:
                cd = form.cleaned_data
                if cd.get("user") == author:
                    author_exist = True
                    if cd.get("role") != "administrator":
                        author_admin_error = True
                    if cd.get("DELETE") is True:
                        delete_error = True
            if (
                author_exist is False
                or delete_error is True
                or author_admin_error is True
            ):
                formset = ManageProjectUserFormset(instance=project)
                return render(
                    request,
                    "mapping/mapping_project_user.html",
                    {
                        "form": formset,
                        "current_proj": current_proj,
                        "data_type": data_type,
                        "current_user": current_user,
                        "data_type": data_type,
                        "mpu_list": mpu_list,
                        "project": project,
                    },
                )
            for form in formset.deleted_forms:
                cd_delete = form.cleaned_data
                user_delete = cd_delete.get("user")
                if user_delete is not None:
                    if user_delete != author:
                        list_delete_user.append(form.cleaned_data)
            if list_delete_user != []:
                obj_to_delete = []
                users_collection = []
                obj_str = ""
                for user in list_delete_user:
                    obj_str = str(obj_str) + str(user.get("id").pk) + ","
                    obj_to_delete.append(user.get("id"))
                    users_collection.append(user.get("user"))
                form = LinkMappingUserForm

                return render(
                    request,
                    "mapping/form_delete_users.html",
                    {
                        "form": form,
                        "obj_to_delete": obj_to_delete,
                        "users": users_collection,
                        "data_type": "user_mapping",
                        "project_id": current_proj,
                        "project": project,
                        "obj_str": obj_str,
                    },
                )
            else:
                for form in formset:
                    cd = form.cleaned_data
                    logger.debug(cd)
                    user = cd.get("user")
                    role = cd.get("role")
                    if user is not None:
                        if user != author:
                            if role == "administrator":
                                assign_perm("view_project", user.user, project)
                                assign_perm("add_project", user.user, project)
                                assign_perm("change_project", user.user, project)
                                assign_perm("delete_project", user.user, project)
                                assign_perm("manage_user", user.user, project)
                                messages.info(
                                    request,
                                    "User "
                                    + str(user.user)
                                    + " set as administrator for project "
                                    + str(project),
                                )
                            elif role == "contributor":
                                assign_perm("view_project", user.user, project)
                                assign_perm("change_project", user.user, project)
                                assign_perm("delete_project", user.user, project)
                                remove_perm("add_project", user.user, project)
                                remove_perm("manage_user", user.user, project)
                                messages.info(
                                    request,
                                    "User "
                                    + str(user.user)
                                    + " set as contributor for project "
                                    + str(project),
                                )
                            elif role == "collaborator":
                                assign_perm("view_project", user.user, project)
                                remove_perm("add_project", user.user, project)
                                remove_perm("change_project", user.user, project)
                                remove_perm("delete_project", user.user, project)
                                messages.info(
                                    request,
                                    "User "
                                    + str(user.user)
                                    + " set as collaborator for project "
                                    + str(project),
                                )
                formset.save()
                return HttpResponseRedirect(
                    reverse("core:mapping_project_user", args=[current_proj])
                )

    else:
        formset = ManageProjectUserFormset(instance=project)

    return render(
        request,
        "mapping/mapping_project_user.html",
        {
            "form": formset,
            "current_proj": current_proj,
            "data_type": data_type,
            "current_user": current_user,
            "data_type": data_type,
            "mpu_list": mpu_list,
            "project": project,
        },
    )


def get_list_mapping_type_of_available_children(list_ressource, data_type, connector):
    i = 0
    list_objects = []
    list_objects_map = []
    for item in list_ressource:
        if item == data_type:
            data_type_map = list_ressource[item]
            i = 1
        else:
            if i == 1:
                list_objects.append(items.get_plural_form_of_type(item))
                for res in list_ressource[item]:
                    list_objects_map.append(connector.get_plural_form_of_type(res))
    return data_type_map, list_objects, list_objects_map
