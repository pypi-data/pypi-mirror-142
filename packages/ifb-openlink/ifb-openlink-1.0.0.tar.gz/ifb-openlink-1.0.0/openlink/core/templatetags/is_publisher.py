from django import template
from openlink.core.connector import Publisher
from openlink.core.models import Tool

# from openlink.core.lib.tools import
register = template.Library()


@register.filter(name="is_publisher")
def is_publisher(instance):
    return issubclass(
        Tool.objects.get(id=instance.id).get_connector().__class__, Publisher
    )
