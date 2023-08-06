from django.contrib import admin

# from django.contrib.admin.options import get_content_type_for_model
# from django.urls import reverse
# from django.utils.html import format_html
# from django.utils.translation import ugettext
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import (
    Assay,
    Dataset,
    Image,
    Investigation,
    Mapping,
    MappingParam,
    MappingProjectUser,
    Profile,
    Project,
    Study,
    Team,
    Tool,
    Toolparam,
)


# Define an inline admin descriptor for Profile model
# which acts a bit like a singleton
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = "profile"


# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)


class ViewOnSiteModelAdmin(admin.ModelAdmin):
    class Media:
        css = {
            "all": (
                "https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css",
            )
        }


class ToolAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "project")


class MappingAdmin(admin.ModelAdmin):
    list_display = ["name", "type", "tag_tool", "author"]


class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "id")


class InvestigationAdmin(admin.ModelAdmin):
    list_display = ["name", "id", "get_project"]


class StudyAdmin(admin.ModelAdmin):
    list_display = ["name", "id", "get_project", "get_investigation"]


class AssayAdmin(admin.ModelAdmin):
    list_display = ["name", "id", "get_project", "get_investigation", "get_study"]


class DatasetAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "id",
        "get_project",
        "get_investigation",
        "get_study",
        "get_assay",
    ]


class MappingProjctUserAdmin(admin.ModelAdmin):
    list_display = ["user", "project", "role"]


admin.site.register(Project, ProjectAdmin)
admin.site.register(Investigation, InvestigationAdmin)
admin.site.register(Study, StudyAdmin)
admin.site.register(Assay, AssayAdmin)
admin.site.register(Dataset, DatasetAdmin)
admin.site.register(Image)
admin.site.register(Team)
admin.site.register(Mapping, MappingAdmin)
admin.site.register(Tool, ToolAdmin)
admin.site.register(Toolparam)
admin.site.register(MappingProjectUser, MappingProjctUserAdmin)
admin.site.register(MappingParam)
admin.site.register(Profile)
