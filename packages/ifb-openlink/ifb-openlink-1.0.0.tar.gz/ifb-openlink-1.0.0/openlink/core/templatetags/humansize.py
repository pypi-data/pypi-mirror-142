from django import template
from openlink.core.views.projects import humansize

register = template.Library()


@register.filter(name="humansize")
def humansizes(nbytes):
    if isinstance(nbytes, int):
        return humansize(nbytes)
    return nbytes
