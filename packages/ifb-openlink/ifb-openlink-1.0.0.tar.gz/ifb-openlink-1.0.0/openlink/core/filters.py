import django_filters

from .models import Assay, Dataset, Investigation, Project, Study


class ProjectFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = Project
        fields = ["name"]


class InvestigationFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = Investigation
        fields = ["name"]


class DatasetFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = Dataset
        fields = ["name"]


class AssayFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = Assay
        fields = ["name"]


class StudyFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = Study
        fields = ["name"]
