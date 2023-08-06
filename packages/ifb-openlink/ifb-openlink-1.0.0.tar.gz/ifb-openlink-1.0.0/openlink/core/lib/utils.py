import logging

from django.contrib import messages
from openlink.core.connector import DataObject
from openlink.core.models import Mapping

logger = logging.getLogger(__name__)


def create_children_mappings(
    request, tool, parent_openlink_object, reference_mapping, container, author
):
    data_type = type(parent_openlink_object)
    data_type_child = data_type.get_child_type()
    connector = tool.get_connector()
    children_data_objects = connector.get_data_objects(
        data_type_child.__name__.lower(), reference_mapping, container
    )
    for child_data_object in children_data_objects:
        if not isinstance(child_data_object, DataObject):
            next
        openlink_object = data_type_child.create_instance(child_data_object, author)
        openlink_object.save()
        messages.info(
            request,
            str(data_type_child.__name__ + " ")
            + str(openlink_object.name)
            + " created ",
        )
        data_type.link_child_to_parent(parent_openlink_object, openlink_object)
        Mapping_openlink_object = Mapping.create_instance(
            openlink_object, child_data_object, tool, author
        )
        Mapping_openlink_object.save()
        messages.info(
            request, "Mapping " + str(Mapping_openlink_object.name) + " created "
        )
        child_type = data_type_child.get_child_type()
        if child_type is not None:
            create_children_mappings(
                request,
                tool,
                openlink_object,
                reference_mapping,
                child_data_object,
                author,
            )


def add_number_at_end_if_name_exist(object_name, update_object):
    if any(
        d.name == object_name
        for d in update_object.get_parent(update_object.id).first().items
    ):
        i = 1
        name = object_name + " (" + str(i) + ")"
        while any(
            d.name == name
            for d in update_object.get_parent(update_object.id).first().items
        ):
            i += 1
            name = object_name + " (" + str(i) + ")"
        new_name = name
    else:
        new_name = object_name
    return new_name
