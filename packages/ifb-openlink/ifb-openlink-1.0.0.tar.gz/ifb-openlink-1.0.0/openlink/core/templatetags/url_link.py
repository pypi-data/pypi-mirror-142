from django import template

# from openlink.core.lib import tools
from openlink.core.models import Mapping

register = template.Library()


@register.filter(name="url_link")
def url_link(obj):
    mapping = Mapping.objects.filter(foreign_id_obj=obj)
    return mapping
