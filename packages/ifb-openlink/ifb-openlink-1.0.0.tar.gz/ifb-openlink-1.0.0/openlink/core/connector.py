import inspect
import logging
import sys
from abc import ABC, abstractmethod
from importlib import import_module

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Button, Submit
from django import forms
from django.conf import settings

logger = logging.getLogger(__name__)

LIST_STRUCTURE = 0
TREE_STRUCTURE = 1


class ToolForm(forms.Form):
    project_id = int

    def __init__(self, *args, **kwargs):
        super(ToolForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_group_wrapper_class = "row"
        self.helper.label_class = "col-sm-offset-1 col-sm-2"
        self.helper.field_class = "col-md-8"
        self.helper.add_input(
            Button(
                "back",
                "Back",
                css_class="btn-secondary",
                onClick="javascript:history.go(-1);",
            )
        )
        self.helper.add_input(Submit("submit", "Add Tool"))

    def clean(self):
        from openlink.core.models import Tool

        cleaned_data = super().clean()
        if "name" in cleaned_data:
            if Tool.objects.filter(
                name=cleaned_data["name"], project_id=self.project_id
            ).first():
                self.add_error("name", "a tool with the same name already exists ")
        return cleaned_data


class BasicObject:
    """Constructor method"""

    def __init__(self, id, name, inner_type, description=None):
        self.id = id
        self.name = name
        self.inner_type = inner_type
        self.description = description


class DataObject(BasicObject):
    """Constructor method"""

    def __init__(self, id, name, inner_type, description=None):
        super().__init__(id, name, inner_type, description)


class ContainerObject(BasicObject):
    """Constructor method"""

    def __init__(self, id, name, inner_type, description=None):
        super().__init__(id, name, inner_type, description)


class ContainerDataObject(DataObject, ContainerObject):
    """Constructor method"""

    def __init__(self, id, name, inner_type, description=None):
        super().__init__(id, name, inner_type, description)


class ToolConnector(ABC):
    """Parent class of all connectors, declares the basic functions of a connector."""

    @classmethod
    @abstractmethod
    def get_name(cls):
        """Return the connector name.

        Returns:
            str: Connector name.
        """
        raise NotImplementedError()

    @classmethod
    @abstractmethod
    def get_creation_form(cls):
        """Returns class used for connector creation form.

        Returns:
            class: Form class needed for connector creation form.
        """
        raise NotImplementedError()

    @classmethod
    @abstractmethod
    def get_edition_form(cls):
        """Returns class used for connector edition form.

        Returns:
            class: Form class needed for connector edit form.
        """
        raise NotImplementedError()

    @classmethod
    @abstractmethod
    def has_access_url(cls):
        """Return True if the mapping object can be accessed online, through an URL.

        Returns:
            bool: True if the mapping object be can be accessed through an URL.
        """
        raise NotImplementedError()

    @classmethod
    @abstractmethod
    def get_logo(cls):
        """Return the static path of the connector logo.

        Returns:
            str: Connector logo static path.
        """
        raise NotImplementedError()

    @classmethod
    def has_mapping_options(cls):
        """Return True if the connector has mapping options.

        Returns:
            bool: True if connector has specific mapping options.
        """
        raise NotImplementedError()

    @abstractmethod
    def get_url_link_to_an_object(self, obj_type, obj_id):
        """Get url link for a given object id and type.

        Arguments:
            obj_type (str): type of the object
            obj_id (int): Id of an object
        Returns:
            str:
            url for a given object
        """
        raise NotImplementedError()


class Mapper(ToolConnector):
    """Parent class for data management connector, declares the minimum
    functions to map a data to openlink.
    """

    @classmethod
    @abstractmethod
    def get_supported_types(cls):
        """A list of tuples with singular ressources name and their
        nomenclature equivalent in Openlink.
        """
        raise NotImplementedError()

    @abstractmethod
    def get_space_info(self, objects_id):
        """Retrieve the size from a list of objects.

        Arguments:
            objects_id (list or None): A list of objects id.
        Returns:
            int: total size of all input objects in bytes.
        """
        raise NotImplementedError()

    @abstractmethod
    def get_investigation(self, object_id):
        """
        Retrieve an object that can be mapped to an Openlink Investigation.

        Arguments:
            object_id (str): Id of an object.
        Returns:
            BasicObject: Instance of a BasicObject containing object id,
            name and description.
        """
        raise NotImplementedError()

    @abstractmethod
    def get_study(self, object_id):
        """Retrieve an object that can be mapped to an Openlink Study.

        Arguments:
            object_id (str): Id of an object.
        Returns:
            BasicObject: name and description.
        """
        raise NotImplementedError()

    @abstractmethod
    def get_assay(self, object_id):
        """Retrieve an object that can be mapped to an Openlink Assay.

        Arguments:
            object_id (str): Id of an object.
        Returns:
            BasicObject: Instance of a BasicObject containing object id,
            name and description.
        """
        pass

    @abstractmethod
    def get_dataset(self, object_id):
        """Retrieve an object that can be mapped to an Openlink Dataset.

        Arguments:
            object_id (str): Id of an object.
        Returns:
            BasicObject: Instance of a BasicObject containing object id,
            name and description.
        """
        raise NotImplementedError()

    @abstractmethod
    def get_investigations(self):
        """Retrieve a list of objects that can be mapped to
            an Openlink Investigation.

        Returns:
            list:  List of Instance of a BasicObject containing object id,
            name and description.
        """
        raise NotImplementedError()

    @abstractmethod
    def get_studies(self, reference_mapping, container):
        """Retrieve a list of objects that can be mapped to an Openlink Studies.

        Arguments:
            reference_mapping (BasicObject): Instance of a BasicObject, needed for the retrival of the objects sought.
            container (BasicObject): Instance of a BasicObject, container of the objects sought.
        Returns:
            list: List of Instance of a BasicObject containing object id,
            name and description.
        """
        raise NotImplementedError()

    @abstractmethod
    def get_assays(self, reference_mapping, container):
        """Retrieve a list of objects that can be mapped to an Openlink Assays.

        Arguments:
            reference_mapping (BasicObject): Instance of a BasicObject, needed for the retrival of the objects sought.
            container (BasicObject): Instance of a BasicObject, container of the objects sought.
        Returns:
            list: List of Instance of a BasicObject containing object id,
            name and description.
        """
        raise NotImplementedError()

    @abstractmethod
    def get_datasets(self, reference_mapping, container):
        """Retrieve a list of objects that can be mapped to an Openlink Datasets.

        Arguments:
            reference_mapping (BasicObject): Instance of a BasicObject, needed for the retrival of the objects sought.
            container (BasicObject): Instance of a BasicObject, container of the objects sought.
        Returns:
            list: List of Instance of a BasicObject containing object id,
            name and description.
        """
        raise NotImplementedError()

    @abstractmethod
    def get_data_object(self, data_type, object_id):
        """Launch a function depending of a given data_type,
        to retrieve an object that can be mapped.

        Arguments:
            data_type (class): Openlink type of an object.
            object_id (str): Id of an object.
        Returns:
            list: List of Instance of a BasicObject containing object id,
            name and description.
        """
        raise NotImplementedError()

    @abstractmethod
    def get_data_objects(self, data_type, reference_mapping=None, container=None):
        """Launch a function depending of a given data_type,
        to retrieve a list of objects that can be mapped.

        Arguments:
            data_type (class): Openlink type of an object.
            reference_mapping (BasicObject): Instance of a BasicObject, needed for the retrival of the objects sought.
            container (BasicObject): Instance of a BasicObject, container of the objects sought.
        Returns:
            list: List of Instance of a BasicObject containing object id,
            name and description.
        """
        raise NotImplementedError()

    @abstractmethod
    def get_plural_form_of_type(self, data_type):
        """Get a plural form of a type of data from Openlink objects.

        Arguments:
            data_type (class): Openlink type of an object.
        Return:
            str: Plural form of a type of data.
        """
        raise NotImplementedError()

    @abstractmethod
    def get_information(self, type, id):
        """retrieves different information from the connector session (author, tags, name).

        Arguments:
            type (str): Openlink type of an object.
            id (str): Id of an object.
        Returns:
            dict: Info about the object, such as tags and user
        """
        raise NotImplementedError()

    @abstractmethod
    def download(self, object_id, path):
        """Download data from an object link in openlink path.

        Arguments:
           object_id (str): Id of an object.
           path (str): Path to where the downloaded files will be stored.
        """
        raise NotImplementedError()


class Publisher(ToolConnector):
    """Parent class for data publishing connectors, declares the minimum
    functions to publish a dataset.
    This class can be modified after each new publisher added.
    """

    @abstractmethod
    def create_empty_depo(self):
        """Initiate a new depository in the publisher.

        Returns:
            json: Json structure sent by api connector requests.
        """
        raise NotImplementedError()

    @abstractmethod
    def add_file_to_depo(self, json, path_to_file):
        """adding file in depository

        Arguments:
            json (json): Json structure sent by api connector requests.
            path_to_file (str): path to the file downloaded by Openlink.
        Returns:
            json: Json structure sent by api connector requests.
        """
        raise NotImplementedError()

    @abstractmethod
    def add_metadata_to_depo(self, meta, jsonr):
        """adding metadata to depository

        Arguments:
            meta (dict): Dictionary of metadata specific of an object from a connector.
            jsonr (str): link to the depo, retrieved from a json object.
        Returns:
            json: Json structure sent by api connector requests.
        """
        raise NotImplementedError()

    @abstractmethod
    def publish_depo(self, json):
        """publish the depository.

        Arguments:
            json (json): Json structure holding a usefull link to publish data.
        Returns:
            json: Json structure sent by api connector requests.
        """
        raise NotImplementedError()


class AuthentificationError(Exception):
    def __init__(self, tool, invalid_item):
        self.message = "invalid " + tool.get_name() + " " + invalid_item
        super().__init__(self.message)


class NotFoundError(Exception):
    def __init__(self, tool):
        self.message = "the " + tool.get_name + " object not found "
        super().__init__(self.message)


class ToolUnreachableError(Exception):
    def __init__(self, tool):
        self.message = (
            tool.get_name() + " server temporarily unavailable, try again later "
        )
        super().__init__(self.message)


class permissionError(Exception):
    def __init__(self, tool):
        self.message = "you do not have the necessary permission for this action"
        super().__init__(self.message)


class defaultError(Exception):
    def __init__(self, tool):
        self.message = "an error has occured on " + tool.get_name()
        super().__init__(self.message)


def find_connectors_in_module(module):
    connectors = []
    for name, obj in inspect.getmembers(module):
        if (
            inspect.isclass(obj)
            and issubclass(obj, ToolConnector)
            and obj is not ToolConnector
            and obj is not Publisher
            and obj is not Mapper
        ):
            connectors.append(obj)
        if inspect.ismodule(obj) and module.__name__ in obj.__name__:
            connectors.extend(find_connectors_in_module(obj))

    return connectors


def get_connectors():
    """Retrieves dynamically all implementation of connectors in apps"""
    connectors = []

    for app_module_name in settings.INSTALLED_APPS:
        connectors_module = None
        connectors_module_name = f"{app_module_name}.connectors"
        if connectors_module_name in sys.modules:
            connectors_module = sys.modules[connectors_module_name]
        else:
            try:
                connectors_module = import_module(connectors_module_name)
            except ModuleNotFoundError:
                pass
                # logger.debug(f'No connectors module in {app_module_name}')

        connectors.extend(find_connectors_in_module(connectors_module))

    return connectors


def get_connector_class(connector_name):
    for connector in get_connectors():
        if connector.__name__ == connector_name:
            return connector

    return None


def get_connector(tool):
    connector_class = get_connector_class(tool.connector)
    return connector_class(tool)
