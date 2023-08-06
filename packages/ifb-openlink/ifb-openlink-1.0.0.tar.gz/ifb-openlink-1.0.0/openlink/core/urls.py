from django.urls import path, register_converter
from openlink.core import views
from openlink.core.views import items, mapping, projects, publish, tools, users


class FloatConverter:
    regex = r"[\d\.\d]+"

    def to_python(self, value):
        return float(value)

    def to_url(self, value):
        return "{}".format(value)


register_converter(FloatConverter, "float")


app_name = "core"
urlpatterns = [
    path("", views.home, name="home"),
    path("profile/<username>/", views.get_user_profile, name="user-profile"),
    path("contact/", views.contact, name="contact"),
    # projects creation
    path("projects", projects.projects, name="projects"),
    path("projects/new", projects.new_project, name="projects-new"),
    path("projects/add", projects.add_project, name="projects-add"),
    # projects tools
    path(
        "projects/<int:project_id>/tools",
        tools.list_tools_project,
        name="tools-project",
    ),
    path(
        "projects/<int:project_id>/tools/new",
        tools.select_connector_project,
        name="select-connector-project",
    ),
    path(
        "projects/<int:project_id>/tools/<str:connector>",
        tools.add_tool_project,
        name="add-tool-project",
    ),
    path(
        "projects/<int:project_id>/tools/<int:tool_id>/edit_toolparam",
        tools.toolsparam_edit_project,
        name="toolsparam-edit-project",
    ),
    path(
        "projects/<int:project_id>/tools/<int:tool_id>/edit_tool",
        tools.ToolUpdate.as_view(),
        name="tools-edit-project",
    ),
    path(
        "projects/<int:project_id>/tool/<int:tool_id>",
        tools.get_tool_info_project,
        name="tool-project",
    ),
    path(
        "projects/<int:project_id>/delete/tool/<int:pk>",
        tools.delete_tool,
        name="delete_tool",
    ),
    path(
        "project/<int:project_id>/<str:data_type>/<int:pk>/choose_tool",
        tools.choose_tool,
        name="choose_tool_project",
    ),
    path(
        "project/<int:project_id>/investigations/<int:investigation_id>/<str:data_type>/<int:pk>/choose_tool",
        tools.choose_tool,
        name="choose_tool_project",
    ),
    # projects editing
    path(
        "projects/<int:project_id>/edit",
        items.ProjectUpdate.as_view(),
        name="edit-project",
    ),
    path(
        "projects/<int:project_id>/add_user_mapping",
        users.add_user_mapping,
        name="add_user_mapping",
    ),
    path(
        "projects/<int:project_id>/manage_user",
        mapping.mapping_project_user,
        name="mapping_project_user",
    ),
    path(
        "projects/<int:project_id>/delete_user_mapping/<str:pk>",
        mapping.delete_user_mapping,
        name="delete_user_mapping",
    ),
    path("projects/<int:project_id>/", projects.details, name="projects-details"),
    path(
        "projects/<int:project_id>/delete/<str:data_type>/<int:pk>",
        projects.delete,
        name="delete",
    ),
    path(
        "projects/<int:project_id>/add_investigation",
        items.add_investigation,
        name="add-investigation",
    ),
    path(
        "projects/<int:project_id>/investigations/<int:investigation_id>/edit",
        items.InvestigationUpdate.as_view(),
        name="edit-investigation",
    ),
    path(
        "projects/<int:project_id>/investigations/<int:investigation_id>/add_study",
        items.add_study,
        name="add-study",
    ),
    path(
        "projects/<int:project_id>/investigations/<int:investigation_id>/study/<int:study_id>/edit",
        items.StudyUpdate.as_view(),
        name="edit-study",
    ),
    # project investigation study assay
    path(
        "projects/<int:project_id>/investigations/<int:investigation_id>/select_study_to_create_assay",
        items.select_study_to_create_assay,
        name="select-study-to-create-assay",
    ),
    path(
        "projects/<int:project_id>/investigations/<int:investigation_id>/study/<int:study_id>/add_assay",
        items.add_assay,
        name="add-assay",
    ),
    path(
        "projects/<int:project_id>/investigations/<int:investigation_id>/assay/<int:assay_id>/edit",
        items.AssayUpdate.as_view(),
        name="edit-assay",
    ),
    # project investigation study assay dataset
    path(
        "projects/<int:project_id>/investigations/<int:investigation_id>/select_assay_to_create_dataset",
        items.select_assay_to_create_dataset,
        name="select-assay-to-create-dataset",
    ),
    path(
        "projects/<int:project_id>/investigations/<int:investigation_id>/assay/<int:assay_id>/add_dataset",
        items.add_dataset,
        name="add-dataset",
    ),
    path(
        "projects/<int:project_id>/investigations/<int:investigation_id>/dataset/<int:dataset_id>/edit",
        items.DatasetUpdate.as_view(),
        name="edit-dataset",
    ),
    # project investigation map_id item
    # path(
    #     "projects/<int:project_id>/investigations/<int:investigation_id>/<str:map_id>/datasets",
    #     mapping.datasets,
    #     name="datasets",
    # ),
    path(
        "projects/<int:project_id>/investigations/<int:investigation_id>/dataset/<int:dataset_id>/<int:tool_id>/<path:map_id>/datasets",
        mapping.datasets,
        name="datasets",
    ),
    path(
        "projects/<int:project_id>/investigations/<int:investigation_id>/assay/<int:assay_id>/<int:tool_id>/<path:map_id>/datasets",
        mapping.datasets,
        name="datasets",
    ),
    path(
        "projects/<int:project_id>/investigations/<int:investigation_id>/<int:tool_id>/<str:map_id>/datasets",
        mapping.datasets,
        name="datasets",
    ),
    path(
        "projects/<int:project_id>/investigations/<int:investigation_id>/study/<int:study_id>/<int:tool_id>/<str:map_id>/assays",
        mapping.assays,
        name="assays",
    ),
    path(
        "projects/<int:project_id>/investigations/<int:investigation_id>/<int:tool_id>/<str:map_id>/assays",
        mapping.assays,
        name="assays",
    ),
    path(
        "projects/<int:project_id>/investigations/<int:investigation_id>/<int:tool_id>/<str:map_id>/studies",
        mapping.studies,
        name="studies",
    ),
    # project investigation map_id select mapping
    path(
        "projects/<int:project_id>/investigations/<int:investigation_id>/<str:map_id>/select_dataset_mapping",
        mapping.select_dataset_mapping,
        name="select_dataset_mapping",
    ),
    path(
        "projects/<int:project_id>/investigations/<int:investigation_id>/<int:tool_id>/<str:map_id>/select_assay_mapping",
        mapping.select_assay_mapping,
        name="select_assay_mapping",
    ),
    # publish
    path(
        "project/<int:project_id>/<str:data_type>/<int:pk>/choose_tool_for_publish",
        tools.choose_tool_for_publish,
        name="choose_tool_for_publish_project",
    ),
    path(
        "project/<int:project_id>/investigations/<int:investigation_id>/<str:data_type>/<int:pk>/choose_tool_for_publish",
        tools.choose_tool_for_publish,
        name="choose_tool_for_publish_project",
    ),
    path(
        "projects/<int:project_id>/<str:data_type>/<int:pk>/<str:tool>/<int:tool_id>/choose_object_to_publish",
        publish.choose_object_to_publish,
        name="choose_object_to_publish",
    ),
    path(
        "projects/<int:project_id>/<str:data_type>/<int:pk>/<str:tool>/<int:tool_id>/update/<path:saved_doi>/choose_object_to_publish",
        publish.choose_object_to_publish,
        name="choose_object_to_publish",
    ),
    path(
        "projects/<int:project_id>/<str:data_type>/<int:pk>/<str:tool>/<int:tool_id>/update/<path:saved_doi>/choose_metadata",
        publish.choose_metadata,
        name="choose_metadata",
    ),
    # testé quelle route est uttilisé pour choose_meta
    path(
        "projects/<int:project_id>/investigations/<int:investigation_id>/<str:data_type>/<int:pk>/choose_metadata",
        publish.choose_metadata,
        name="choose_metadata",
    ),
    path(
        "projects/<int:project_id>/<str:data_type>/<int:pk>/<str:tool>/<int:tool_id>/choose_metadata",
        publish.choose_metadata,
        name="choose_metadata",
    ),
    path(
        "projects/<int:project_id>/investigations/<int:investigation_id>/<str:data_type>/<int:pk>/<str:tool>/<int:tool_id>/choose_metadata",
        publish.choose_metadata,
        name="choose_metadata",
    ),
    # path(
    #     "projects/<int:project_id>/investigations/<int:investigation_id>/<str:data_type>/<int:pk>/choose_non_linked_object",
    #     mapping.choose_non_linked_object,
    #     name="choose_non_linked_object",
    # ),
    path(
        "projects/<int:project_id>/<str:data_type>/<int:pk>/<int:tool_id>/choose_non_linked_object",
        mapping.choose_non_linked_object_tool,
        name="choose_non_linked_object_tool",
    ),
    path(
        "projects/<int:project_id>/investigations/<int:investigation_id>/<str:data_type>/<int:pk>/<int:tool_id>/choose_non_linked_object",
        mapping.choose_non_linked_object_tool,
        name="choose_non_linked_object_tool",
    ),
    path(
        "projects/<int:project_id>/<str:data_type>/<int:pk>/<str:tool>/<int:tool_id>/choose_non_linked_object",
        mapping.choose_non_linked_object_tool,
        name="choose_non_linked_object_tool",
    ),
    path(
        "projects/<int:project_id>/investigations/<int:investigation_id>/<str:data_type>/<int:pk>/<str:tool>/<int:tool_id>/choose_non_linked_object",
        mapping.choose_non_linked_object_tool,
        name="choose_non_linked_object_tool",
    ),
    # path('projects/<int:id>/investigations/<int:investigation_id>/<str:data_type>/<int:pk>/choose_object_to_publish', projects.choose_object_to_publish, name='choose_object_to_publish'),
    # path('projects/<int:id>/investigations/<int:investigation_id>/<str:data_type>/<int:pk>/<str:tool>/<int:tool_id>/choose_object_to_publish', projects.choose_object_to_publish, name='choose_object_to_publish'),
    path(
        "projects/<int:project_id>/investigations/<int:investigation_id>/<str:data_type>/<int:pk>/<int:tool_id>/<path:map_id>/choose_option_mapping",
        mapping.choose_option_mapping,
        name="choose_option_mapping",
    ),
    path(
        "projects/<int:project_id>/investigations/<int:investigation_id>/<str:data_type>/<int:tool_id>/<path:map_id>/choose_option_mapping",
        mapping.choose_option_mapping,
        name="choose_option_mapping",
    ),
    path(
        "projects/<int:project_id>/investigations/<int:investigation_id>/<int:tool_id>/<path:map_id>/choose_option_mapping",
        mapping.choose_option_mapping,
        name="choose_option_mapping",
    ),
    path(
        "projects/<int:project_id>/investigations/<int:investigation_id>/delete/<str:data_type>/<int:pk>",
        projects.delete,
        name="delete",
    ),
    path(
        "projects/<int:project_id>/investigations/<int:investigation_id>/delete/mapping/<str:data_type>/<int:pk>",
        mapping.delete_mapping,
        name="delete-mapping",
    ),
    path(
        "tool/<int:tool_id>/<str:data_type>/<path:map_id>",
        items.get_json_object,
        name="get_json_object",
    ),
    # projects/<int:project_id>/investigations/<int:investigation_id>/assay/<int:assay_id>/<path:map_id>/datasets
]
