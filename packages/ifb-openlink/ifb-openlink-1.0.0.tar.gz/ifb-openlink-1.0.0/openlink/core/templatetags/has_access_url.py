from django import template
from openlink.core.models import Tool

# from openlink.core.lib.tools import
register = template.Library()


@register.filter(name="has_access_url")
def has_access_url(instance):
    connector = Tool.objects.get(id=instance.id).get_connector()
    return connector.has_access_url()
