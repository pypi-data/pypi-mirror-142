import logging
from datetime import datetime

from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.forms import ModelChoiceField
from django.shortcuts import get_object_or_404
from django.utils import timezone
from openlink.core.connector import get_connector

logger = logging.getLogger(__name__)


class Team(models.Model):
    name = models.CharField(max_length=100, blank=True)
    date = models.DateTimeField(default=datetime.now, blank=True, null=True)

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    team = models.ManyToManyField(Team, blank=True)

    def __str__(self):
        return str(self.user)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Mappableobject(models.Model):
    def __str__(self):
        return str(self.id)

    @property
    def type(self):
        return self._meta.model_name

    @classmethod
    def create(cls, form, profile, parent_id):
        logger.debug("create")
        item = form.save(commit=False)
        item.author = profile
        item.date_created = timezone.now()
        item.save()

        parent_type = cls.get_parent_type()
        parent_item = getattr(parent_type, "get_" + parent_type.__name__.lower())(
            parent_id
        ).first()

        getattr(parent_item, item.get_plural()).add(item)
        parent_item.save()

        return item


class Image(Mappableobject):
    name = models.CharField(max_length=100, blank=True)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class Dataset(Mappableobject):
    name = models.CharField(max_length=100)
    description = RichTextField(
        blank=True, null=True, config_name="zenodo"
    )  # models.TextField(blank=True, null=True)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name

    def get_plural(self):
        return "datasets"

    @staticmethod
    def get_parent(id):
        return Assay.objects.filter(datasets__id=id)

    def get_dataset(id):
        return Dataset.objects.filter(id=id)

    def get_assay(id):
        id = id.id if type(id) == Dataset else id
        return Assay.objects.filter(datasets__id=id)

    def get_study(id):
        id = id.id if type(id) == Dataset else id
        return Study.objects.filter(assays__datasets__id=id)

    def get_investigation(id):
        id = id.id if type(id) == Dataset else id
        return Investigation.objects.filter(studies__assays__datasets__id=id)

    def get_project(id):
        id = id.id if type(id) == Dataset else id
        return Project.objects.filter(investigations__studies__assays__datasets__id=id)

    def get_parent_type():
        return Assay

    def get_child_type():
        return None

    def model_plural():
        return "datasets"

    @classmethod
    def create_instance(cls, child_data_object, author):
        New_dataset = cls()
        New_dataset.name = child_data_object.name
        New_dataset.description = child_data_object.description
        New_dataset.author = author
        New_dataset.date_created = timezone.now()
        return New_dataset


class Assay(Mappableobject):
    name = models.CharField(max_length=100)
    description = RichTextField(
        blank=True, null=True, config_name="zenodo"
    )  # models.TextField(blank=True, null=True)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    datasets = models.ManyToManyField(Dataset, blank=True)

    def __str__(self):
        return self.name

    def get_plural(self):
        return "assays"

    @staticmethod
    def get_parent(id):
        return Study.objects.filter(assays__id=id)

    def get_dataset(id):
        return Dataset.objects.filter(assay__id=id)

    def get_assay(id):
        return Assay.objects.filter(id=id)

    def get_study(id):
        id = id.id if type(id) == Assay else id
        return Study.objects.filter(assays__id=id)

    def get_investigation(id):
        id = id.id if type(id) == Assay else id
        return Investigation.objects.filter(studies__assays__id=id)

    def get_project(id):
        id = id.id if type(id) == Assay else id
        return Project.objects.filter(investigations__studies__assays__id=id)

    @property
    def items(self):
        return list(self.datasets.all())

    def get_parent_type():
        return Study

    def get_child_type():
        return Dataset

    def model_plural():
        return "assays"

    @classmethod
    def create_instance(cls, child_data_object, author):
        New_assay = cls()
        New_assay.name = child_data_object.name
        New_assay.description = child_data_object.description
        New_assay.author = author
        New_assay.date_created = timezone.now()
        return New_assay

    def link_child_to_parent(parent_data_object, child_data_object):
        parent_data_object.datasets.add(child_data_object)


class Study(Mappableobject):
    name = models.CharField(max_length=100)
    description = RichTextField(
        blank=True, null=True, config_name="zenodo"
    )  # models.TextField(blank=True, null=True)
    author = models.ForeignKey(
        Profile, on_delete=models.CASCADE, null=True, related_name="studies"
    )
    date_created = models.DateTimeField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    assays = models.ManyToManyField(Assay, blank=True)

    def __str__(self):
        return self.name

    @property
    def items(self):
        return list(self.assays.all())

    def get_plural(self):
        return "studies"

    @staticmethod
    def get_parent(id):
        return Investigation.objects.filter(studies__id=id)

    def get_dataset(id):
        return Dataset.objects.filter(assay__study__id=id)

    def get_assay(id):
        return Assay.objects.filter(study__id=id)

    def get_study(id):
        return Study.objects.filter(id=id)

    def get_investigation(id):
        id = id.id if type(id) == Study else id
        return Investigation.objects.filter(studies__id=id)

    def get_project(id):
        id = id.id if type(id) == Study else id
        return Project.objects.filter(investigations__studies__id=id)

    def get_parent_type():
        return Investigation

    def get_child_type():
        return Assay

    def model_plural():
        return "studies"

    @classmethod
    def create_instance(cls, child_data_object, author):
        New_study = cls()
        New_study.name = child_data_object.name
        New_study.description = child_data_object.description
        New_study.author = author
        New_study.date_created = timezone.now()
        return New_study

    def link_child_to_parent(parent_data_object, child_data_object):
        parent_data_object.assays.add(child_data_object)


class Investigation(Mappableobject):
    name = models.CharField(max_length=100)
    description = RichTextField(
        blank=True, null=True, config_name="zenodo"
    )  # models.TextField(blank=True, null=True)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    studies = models.ManyToManyField(Study, blank=True)

    def __str__(self):
        return self.name

    @property
    def items(self):
        return list(self.studies.all())

    def get_plural(self):
        return "investigations"

    @staticmethod
    def get_parent(id):
        return Project.objects.filter(investigations__id=id)

    def get_dataset(id):
        return Dataset.objects.filter(assay__study__investigation__id=id)

    def get_assay(id):
        return Assay.objects.filter(study__investigation__id=id)

    def get_study(id):
        return Study.objects.filter(investigation__id=id)

    def get_investigation(id):
        return Investigation.objects.filter(id=id)

    def get_project(id):
        id = id.id if type(id) == Investigation else id
        return Project.objects.filter(investigations__id=id)

    def get_parent_type():
        return Project

    def get_child_type():
        return Study

    def model_plural():
        return "investigations"

    @classmethod
    def create_instance(cls, child_data_object, author):
        New_investigation = cls()
        New_investigation.name = child_data_object.name
        New_investigation.description = child_data_object.description
        New_investigation.author = author
        New_investigation.date_created = timezone.now()
        return New_investigation

    def link_child_to_parent(parent_data_object, child_data_object):
        parent_data_object.studies.add(child_data_object)


class Project(Mappableobject):
    name = models.CharField(max_length=100)
    description = RichTextField(
        blank=True, null=True, config_name="zenodo"
    )  # models.TextField(blank=True, null=True)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    investigations = models.ManyToManyField(Investigation, blank=True)

    class Meta:
        permissions = (("manage_user", "Manage user"),)

    def __str__(self):
        return self.name

    def get_plural(self):
        return "projects"

    def get_dataset(id):
        return Dataset.objects.filter(assay__study__investigation__project__id=id)

    def get_assay(id):
        return Assay.objects.filter(study__investigation__project__id=id)

    def get_study(id):
        return Study.objects.filter(investigation__project__id=id)

    def get_investigation(id):
        return Investigation.objects.filter(project__id=id)

    def get_project(id):
        return Project.objects.filter(id=id)

    @property
    def items(self):
        return list(self.investigations.all())

    def get_child_type():
        return Investigation

    def model_plural():
        return "projects"

    @classmethod
    def create_instance(cls, child_data_object, author):
        New_project = cls()
        New_project.name = child_data_object.name
        New_project.description = child_data_object.description
        New_project.author = author
        New_project.date_created = timezone.now()
        return New_project

    def link_child_to_parent(parent_data_object, child_data_object):
        parent_data_object.investigations.add(child_data_object)


class MappingProjectUser(models.Model):
    ADMINISTRATOR = "administrator"
    CONTRIBUTOR = "contributor"
    COLLABORATOR = "collaborator"
    STATUS = [
        (ADMINISTRATOR, "administrator"),
        (CONTRIBUTOR, "contributor"),
        (COLLABORATOR, "collaborator"),
    ]
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)
    role = models.CharField(
        max_length=13,
        choices=STATUS,
        default=ADMINISTRATOR,
    )

    def __str__(self):
        return str(self.project) + "_" + str(self.user)


class Tool(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    connector = models.CharField(max_length=100, blank=True, null=True)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.id)

    def get_param(self, key):
        value = Toolparam.objects.values_list("value", flat=True).get(
            key=key, tool_id_id=str(self.id)
        )
        return value

    def get_connector(self):
        return get_connector(self)

    @property
    def tag_tool(self):
        connector = self.get_connector()
        tool_tag = connector.get_name()
        return tool_tag


class Toolparam(models.Model):
    tool_id = models.ForeignKey(Tool, on_delete=models.CASCADE, null=True)
    key = models.CharField(max_length=100, blank=True, null=True)
    value = models.CharField(max_length=2000, blank=True, null=True)

    def __str__(self):
        return "%s %s" % (self.key, self.tool_id)


class ToolparamChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.value


class Mapping(models.Model):
    name = models.CharField(max_length=100, blank=True)
    tool_id = models.ForeignKey(Tool, on_delete=models.CASCADE, blank=True, null=True)
    type = models.CharField(max_length=100)
    object_id = models.CharField(max_length=100, blank=True, null=True)
    size = models.BigIntegerField(blank=True, null=True)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    foreign_id_obj = models.ForeignKey(
        Mappableobject, on_delete=models.CASCADE, null=True
    )

    def __str__(self):
        return self.name

    @classmethod
    def create_instance(cls, openlink_object, data_object, tool, author):
        mapping_object = Mapping()
        mapping_object.name = str(data_object.name)
        mapping_object.tool_id = tool
        mapping_object.type = type(openlink_object).__name__.lower()
        mapping_object.object_id = str(data_object.id)
        if type(openlink_object) == Dataset:
            connector = tool.get_connector()
            mapping_object.size = connector.get_space_info([str(data_object.id)])
        mapping_object.author = author
        mapping_object.foreign_id_obj = openlink_object
        return mapping_object

    @property
    def link_name(self):
        tool_qs = get_object_or_404(Tool, id=self.tool_id.id)
        connector = tool_qs.get_connector()
        try:
            object_info = connector.get_object(self.object_id, self.type)
            return object_info["name"]
        except Exception:
            return None

    @property
    def link_url(self):
        tool_qs = get_object_or_404(Tool, id=self.tool_id.id)
        connector = tool_qs.get_connector()
        return connector.get_url_link_to_an_object(self.type, self.object_id)

    @property
    def link_tool(self):
        tool_qs = get_object_or_404(Tool, id=self.tool_id.id)
        tool_name = tool_qs.name
        return tool_name

    @property
    def tag_tool(self):
        tool_qs = get_object_or_404(Tool, id=self.tool_id.id)
        connector = tool_qs.get_connector()
        tool_tag = connector.get_name
        return tool_tag

    @property
    def connector_class(self):
        tool_qs = get_object_or_404(Tool, id=self.tool_id.id)
        return tool_qs.get_connector()

    @property
    def get_supported_types_plural(self):
        from openlink.core.views import items

        data_type = self.type
        connector = self.connector_class
        ressource = connector.get_supported_types()
        ressources = {}
        i = 0
        for key in ressource:
            list_res_plural = []
            if key == data_type:
                i = 1
            else:
                if i == 1:
                    for value in ressource[key]:
                        list_res_plural.append(connector.get_plural_form_of_type(value))
                    ressources[items.get_plural_form_of_type(key)] = list_res_plural
        return ressources

    @property
    def get_supported_types(self):
        return self.connector_class.get_supported_types()


class MappingParam(models.Model):
    mapping_id = models.ForeignKey(Mapping, on_delete=models.CASCADE, null=True)
    key = models.CharField(max_length=100, blank=True, null=True)
    value = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return "%s %s" % (self.key, self.mapping_id)
