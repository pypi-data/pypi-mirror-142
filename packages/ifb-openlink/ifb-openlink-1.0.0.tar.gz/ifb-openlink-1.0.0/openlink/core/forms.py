import logging

from crispy_forms.helper import FormHelper
from crispy_forms.layout import HTML, Button, Field, Fieldset, Layout, Submit
from django import forms
from openlink.core import connector as tools

from .models import (
    Assay,
    Dataset,
    Investigation,
    Mapping,
    MappingProjectUser,
    Project,
    Study,
    Tool,
)

# from django.forms import fields

logger = logging.getLogger(__name__)


class BaseForm(forms.Form):
    parent_id = int

    def __init__(self, *args, **kwargs):
        super(BaseForm, self).__init__(*args, **kwargs)
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

    def clean(self):
        clean_data = super().clean()
        name = clean_data["name"]
        type_class = (
            str(self.__class__)
            .replace("<class 'openlink.core.forms.", "")
            .replace("Form'>", "")
        )
        if not type_class == "Project":
            parent_type = eval(type_class).get_parent_type()
            if not type(self.parent_id) == type:
                parent = getattr(parent_type, "get_" + parent_type.__name__.lower())(
                    self.parent_id
                )
                same_level = parent.first().items
                if any(d.name == name for d in same_level):
                    self.add_error(
                        "name",
                        "a " + type_class + " with the same name already exist",
                    )


class SelectObjectTool(forms.Form):
    object_name = forms.ChoiceField(choices=(), label="unlinked_objects")

    def __init__(self, unlinked_objects=None, *args, **kwargs):
        super(SelectObjectTool, self).__init__(*args, **kwargs)
        self.fields["object_name"].widget = forms.RadioSelect()

        if unlinked_objects:
            self.fields["object_name"].choices = unlinked_objects


class SelectMultipleObjectOption(forms.Form):
    def __init__(self, *args, **kwargs):
        list_objects = kwargs.pop("list_objects")
        list_objects_map = kwargs.pop("list_objects_map")
        data_type_map = kwargs.pop("data_type_map")[0]
        has_mapping_options = kwargs.pop("has_mapping_options")
        connector = kwargs.pop("tool_connector")
        action = kwargs.pop("action")
        super(SelectMultipleObjectOption, self).__init__(*args, **kwargs)
        if len(list_objects_map) > 0:
            self.fields["create_and_link_children"] = forms.BooleanField(
                widget=forms.CheckboxInput(),
                required=False,
                label='Create and link any %s available in "%s"'
                % (" ".join(str(x) for x in list_objects_map), data_type_map),
                help_text="Get links from the content of the %s and create %s in Openlink"
                % (data_type_map, " ".join(str(x) for x in list_objects)),
            )
        if has_mapping_options:
            list_extra_options = connector.get_fields_option_mapping(self.fields)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.form_action = action
        self.helper.layout = Layout(
            HTML(
                """
                <h4 class="display-titre" style="background-color: rgb(255, 255, 255)">Choose options for selected {% for value in data_type_map %}{{value}}{% if not forloop.last %} or{% endif %}{% endfor %}
                {{object_name}}</h4>
                <br>
                """
            ),
            Field("create_and_link_children"),
        )
        if has_mapping_options:
            list_extra_options = connector.get_fields_option_mapping(self.fields)
            self.helper.layout.append(
                Fieldset("{{tool_name}} options", *list_extra_options),
            )
        else:
            if len(self.fields) == 0:
                self.helper.layout.append(
                    Layout(
                        HTML(
                            """
                        {% if not has_mapping_options %}
                            <h6>There are no options to display, please proceed.</h6>
                        {% endif %}
                        """
                        ),
                    )
                )


class SelectObjectOption(forms.Form):

    replace_openlink_name = forms.BooleanField(
        widget=forms.CheckboxInput(), required=False
    )
    use_description = forms.BooleanField(
        label="Use this description", widget=forms.CheckboxInput(), required=False
    )
    add_description = forms.BooleanField(
        label="Add this description to current description",
        widget=forms.CheckboxInput(),
        required=False,
    )

    def __init__(self, *args, **kwargs):
        data_type = kwargs.pop("data_type")
        list_objects = kwargs.pop("list_objects")
        list_objects_map = kwargs.pop("list_objects_map")
        data_type_map = kwargs.pop("data_type_map")[0]
        object_name = kwargs.pop("object_name")
        has_mapping_options = kwargs.pop("has_mapping_options")
        object_desc = kwargs.pop("object_desc")
        connector = kwargs.pop("tool_connector")
        action = kwargs.pop("action")
        super(SelectObjectOption, self).__init__(*args, **kwargs)
        self.fields[
            "replace_openlink_name"
        ].label = 'Replace openlink %s name by "%s"' % (data_type, object_name)
        self.fields[
            "replace_openlink_name"
        ].help_text = 'Update the %s name with the name of the %s "%s"' % (
            data_type,
            data_type_map,
            object_name,
        )
        self.fields["use_description"].help_text = (
            "Use the description found by openlink as description for the current %s"
            % (data_type)
        )
        self.fields["add_description"].help_text = (
            "Add the description found by openlink to the already existing %s description"
            % (data_type)
        )
        if len(list_objects_map) > 0:
            self.fields["create_and_link_children"] = forms.BooleanField(
                widget=forms.CheckboxInput(),
                required=False,
                label='Create and link any %s available in "%s"'
                % (" ".join(str(x) for x in list_objects_map), object_name),
                help_text="Get links from the content of the %s and create %s in Openlink"
                % (data_type_map, " ".join(str(x) for x in list_objects)),
            )

        if not object_desc:
            self.fields["use_description"].widget.attrs["disabled"] = True
            self.fields["add_description"].widget.attrs["disabled"] = True
        if has_mapping_options:
            list_extra_options = connector.get_fields_option_mapping(self.fields)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.form_action = action
        self.helper.layout = Layout(
            HTML(
                """
                <h4 class="display-titre" style="background-color: rgb(255, 255, 255)">Select options for the selected {% for value in data_type_map %}{{value}}{% if not forloop.last %} or{% endif %}{% endfor %}
                {{object_name}}:</h4>
                """
            ),
            Field("replace_openlink_name"),
            Field("create_and_link_children"),
            HTML(
                """
                <h4 class="display-titre" style="background-color: rgb(255, 255, 255)">Description options </h4>
                """
            ),
            Field("use_description"),
            Field("add_description"),
            HTML(
                """
                {% if object_desc %}
                Description found for this {% for value in data_type_map %}{{value}}{% if not forloop.last %} or{% endif %}{% endfor %} {{object_name}}:
                <div class="description_found">
                    {{ object_desc | safe }}
                </div>
                {% endif %}
                <br>"""
            ),
        )
        if has_mapping_options:
            list_extra_options = connector.get_fields_option_mapping(self.fields)
            self.helper.layout.append(
                Fieldset("{{tool_name}} options", *list_extra_options),
            )


class ProjectForm(BaseForm, forms.ModelForm):
    class Meta:
        model = Project
        fields = ["name", "description"]

        widgets = {
            "description": forms.Textarea(attrs={"rows": 3, "cols": 20}),
        }

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        self.helper.add_input(Submit("submit", "Add project", css_class="btn-primary"))


class InvestigationForm(BaseForm, forms.ModelForm):
    class Meta:
        model = Investigation
        fields = ["name", "description"]

        widgets = {
            "description": forms.Textarea(attrs={"rows": 3, "cols": 20}),
        }

    def __init__(self, *args, **kwargs):
        super(InvestigationForm, self).__init__(*args, **kwargs)
        self.helper.add_input(
            Submit("submit", "Add investigation", css_class="btn-primary")
        )


class StudyForm(BaseForm, forms.ModelForm):
    class Meta:
        model = Study
        fields = ["name", "description"]

    def __init__(self, *args, **kwargs):
        super(StudyForm, self).__init__(*args, **kwargs)
        self.helper.add_input(Submit("submit", "Add Study", css_class="btn-primary"))


class SelectStudyForm(forms.Form):
    studies_name = forms.ModelChoiceField(queryset=Study.objects.all())

    def __init__(self, *args, **kwargs):
        investigation = kwargs.pop("instance")
        super(SelectStudyForm, self).__init__(*args, **kwargs)
        self.fields["studies_name"].widget = forms.Select()

        if investigation:
            self.fields["studies_name"].queryset = investigation.studies.all()


class SelectAssayForm(forms.Form):
    assays_name = forms.ModelChoiceField(queryset=Assay.objects.all())

    def __init__(self, *args, **kwargs):
        investigation = kwargs.pop("instance")
        super(SelectAssayForm, self).__init__(*args, **kwargs)
        self.fields["assays_name"].widget = forms.Select()

        if investigation:
            investigation_id = investigation.id
            self.fields["assays_name"].queryset = Assay.objects.filter(
                study__investigation__id=investigation_id
            )


class AssayForm(BaseForm, forms.ModelForm):
    class Meta:
        model = Assay
        fields = ("name", "description")
        widgets = {
            "description": forms.Textarea(attrs={"rows": 3, "cols": 20}),
        }

    def __init__(self, *args, **kwargs):
        super(AssayForm, self).__init__(*args, **kwargs)
        self.helper.add_input(Submit("submit", "Add assay", css_class="btn-primary"))


class DatasetForm(BaseForm, forms.ModelForm):
    class Meta:
        model = Dataset
        fields = ["name", "description"]
        widgets = {
            "description": forms.Textarea(attrs={"rows": 3, "cols": 20}),
        }

    def __init__(self, *args, **kwargs):
        super(DatasetForm, self).__init__(*args, **kwargs)
        self.helper.add_input(Submit("submit", "Add dataset", css_class="btn-primary"))


class ToolForm(forms.Form):

    connectors = [
        (connector.__name__, connector.get_name())
        for connector in tools.get_connectors()
    ]

    connector = forms.ChoiceField(choices=connectors, required=True)
    name = forms.CharField(
        initial=connectors[0][1], label="Name", max_length=100, required=True
    )

    def clean(self):
        cleaned_data = super().clean()
        logger.debug(cleaned_data)
        if Tool.objects.filter(
            name=cleaned_data["name"], project_id=self.project_id
        ).first():
            self.add_error("name", "a tool with the same name already exists ")
        return cleaned_data


class ToolProjectForm(forms.ModelForm, BaseForm):
    class Meta:
        model = Tool
        fields = [
            "name",
        ]

    def __init__(self, *args, **kwargs):
        super(ToolProjectForm, self).__init__(*args, **kwargs)
        self.helper.add_input(Submit("submit", "Add tool", css_class="btn-primary"))


class SelectToolForm(forms.Form):
    Name = forms.ChoiceField(choices=[], required=True)

    def __init__(self, *args, **kwargs):
        tool_list = kwargs.pop("instance")
        super(SelectToolForm, self).__init__(*args, **kwargs)
        self.fields["Name"].widget = forms.RadioSelect()
        tools_choices = []
        for tool in tool_list:
            tools_choices.append((tool.id, tool.get_param("url")))

        self.fields["Name"].choices = tools_choices


class SelectProjectTool(forms.Form):

    project_name = forms.ChoiceField(choices=(), label="Projects")
    replace_openlink_object_name = forms.BooleanField(
        widget=forms.CheckboxInput(), required=False
    )

    def __init__(self, projects=None, *args, **kwargs):
        super(SelectProjectTool, self).__init__(*args, **kwargs)
        self.fields["project_name"].widget = forms.RadioSelect()
        if projects:
            self.fields["project_name"].choices = projects


class SelectInvestigationTool(forms.Form):

    investigation_name = forms.ChoiceField(choices=(), label="Investigations")
    replace_openlink_investigation_name = forms.BooleanField(
        widget=forms.CheckboxInput(), required=False
    )
    create_associated_objects_in_openlink = forms.BooleanField(
        widget=forms.CheckboxInput(), required=False
    )

    def __init__(self, investigations=None, *args, **kwargs):
        super(SelectInvestigationTool, self).__init__(*args, **kwargs)
        self.fields["investigation_name"].widget = forms.RadioSelect()
        if investigations:
            self.fields["investigation_name"].choices = investigations


class SelectInvestigationToolMapping(forms.Form):

    investigation_name = forms.ChoiceField(choices=(), label="Investigations")

    def __init__(self, investigations=None, *args, **kwargs):
        super(SelectInvestigationToolMapping, self).__init__(*args, **kwargs)
        self.fields["investigation_name"].widget = forms.RadioSelect()
        if investigations:
            self.fields["investigation_name"].choices = investigations


class SelectProjectToolMapping(forms.Form):

    project_name = forms.ChoiceField(choices=(), label="Projects")

    def __init__(self, projects=None, *args, **kwargs):
        super(SelectProjectToolMapping, self).__init__(*args, **kwargs)
        self.fields["project_name"].widget = forms.RadioSelect()
        if projects:
            self.fields["project_name"].choices = projects


class SelectStudyTool(forms.Form):

    study_name = forms.ChoiceField(choices=(), label="Studies")
    replace_openlink_study_name = forms.BooleanField(
        widget=forms.CheckboxInput(), required=False
    )

    def __init__(self, studies=None, *args, **kwargs):
        super(SelectStudyTool, self).__init__(*args, **kwargs)
        self.fields["study_name"].widget = forms.RadioSelect()
        if studies:
            self.fields["study_name"].choices = studies


class SelectStudiesTool(forms.Form):

    study_name = forms.ChoiceField(choices=(), label="Studies")

    def __init__(self, studies=None, *args, **kwargs):
        super(SelectStudiesTool, self).__init__(*args, **kwargs)
        self.fields["study_name"].widget = forms.CheckboxSelectMultiple()
        if studies:
            self.fields["study_name"].choices = studies


class SelectAssayTool(forms.Form):

    assay_name = forms.ChoiceField(choices=(), label="Assays")
    replace_openlink_assay_name = forms.BooleanField(
        widget=forms.CheckboxInput(), required=False
    )
    create_associated_objects_in_openlink = forms.BooleanField(
        widget=forms.CheckboxInput(), required=False
    )

    def __init__(self, assays=None, *args, **kwargs):
        super(SelectAssayTool, self).__init__(*args, **kwargs)
        self.fields["assay_name"].widget = forms.RadioSelect()
        if assays:
            self.fields["assay_name"].choices = assays


class SelectAssaysTool(forms.Form):

    assay_name = forms.ChoiceField(choices=(), label="Assay")

    def __init__(self, assays=None, *args, **kwargs):
        super(SelectAssaysTool, self).__init__(*args, **kwargs)
        self.fields["assay_name"].widget = forms.CheckboxSelectMultiple()

        if assays:
            self.fields["assay_name"].choices = assays


class SelectDatasetTool(forms.Form):

    dataset_name = forms.ChoiceField(choices=(), label="Datasets")
    replace_openlink_dataset_name = forms.BooleanField(
        widget=forms.CheckboxInput(), required=False
    )
    synchronize_dataset_with_experiment = forms.BooleanField(
        widget=forms.CheckboxInput(), required=False
    )

    def __init__(self, datasets=None, *args, **kwargs):
        super(SelectDatasetTool, self).__init__(*args, **kwargs)
        self.fields["dataset_name"].widget = forms.RadioSelect()

        if datasets:
            self.fields["dataset_name"].choices = datasets


class SelectDatasetsTool(forms.Form):

    dataset_name = forms.ChoiceField(choices=(), label="Datasets")

    def __init__(self, datasets=None, *args, **kwargs):
        super(SelectDatasetsTool, self).__init__(*args, **kwargs)
        self.fields["dataset_name"].widget = forms.CheckboxSelectMultiple()
        if datasets:
            self.fields["dataset_name"].choices = datasets


class LinkProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = [
            "name",
        ]


class LinkInvestigationForm(forms.ModelForm):
    class Meta:
        model = Investigation
        fields = [
            "name",
        ]


class LinkDatasetForm(forms.ModelForm):
    class Meta:
        model = Dataset
        fields = [
            "name",
        ]


class LinkAssayForm(forms.ModelForm):
    class Meta:
        model = Assay
        fields = [
            "name",
        ]


class LinkStudyForm(forms.ModelForm):
    class Meta:
        model = Study
        fields = [
            "name",
        ]


class LinkToolForm(forms.ModelForm):
    class Meta:
        model = Tool
        fields = [
            "name",
        ]


class LinkMappingForm(forms.ModelForm):
    class Meta:
        model = Mapping
        fields = [
            "name",
        ]


class LinkMappingUserForm(forms.ModelForm):
    class Meta:
        model = MappingProjectUser
        fields = [
            "role",
        ]


class SelectAssaysForm(forms.Form):
    assays_name = forms.ModelChoiceField(queryset=Assay.objects.all())

    def __init__(self, *args, **kwargs):
        investigation = kwargs.pop("investigation")
        super(SelectAssaysForm, self).__init__(*args, **kwargs)
        self.fields["assays_name"].widget = forms.RadioSelect()

        if investigation:
            self.fields["assays_name"].queryset = Assay.objects.filter(
                study__investigation__id=investigation.id
            )


class SelectStudiesForm(forms.Form):
    studies_name = forms.ModelChoiceField(queryset=Study.objects.all())

    def __init__(self, *args, **kwargs):
        investigation = kwargs.pop("investigation")
        super(SelectStudiesForm, self).__init__(*args, **kwargs)
        self.fields["studies_name"].widget = forms.RadioSelect()

        if investigation:
            self.fields["studies_name"].queryset = Study.objects.filter(
                investigation__id=investigation.id
            )


ADMINISTRATOR = "administrator"
CONTRIBUTOR = "contributor"
COLLABORATER = "collaborater"
STATUS = [
    (ADMINISTRATOR, "administrator"),
    (CONTRIBUTOR, "contributor"),
    (COLLABORATER, "collaborater"),
]


class ManageProjectUserForm(forms.Form):
    role = forms.ChoiceField(choices=STATUS)

    def __init__(self, *args, **kwargs):
        project = kwargs.pop("project")
        super(ManageProjectUserForm, self).__init__(*args, **kwargs)

        if project:
            self.initial["role"] = MappingProjectUser.objects.get(project=project)


class AddProjectUserForm(forms.ModelForm):
    class Meta:
        model = MappingProjectUser
        fields = ("user", "role")

    def __init__(self, *args, **kwargs):
        super(AddProjectUserForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_group_wrapper_class = "row"
        self.helper.label_class = "col-sm-offset-1 col-sm-2"
        self.helper.field_class = "col-md-8"
        self.helper.add_input(Submit("submit", "Add", css_class="btn-primary"))
