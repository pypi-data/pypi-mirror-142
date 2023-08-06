from django import template
from openlink.core.models import Assay

register = template.Library()


@register.filter(name="contains_assay")
def contains_assay(obj):
    contains = False
    list_assays = Assay.objects.filter(study__investigation__id=obj.id)
    if list_assays:
        contains = True
    return contains
