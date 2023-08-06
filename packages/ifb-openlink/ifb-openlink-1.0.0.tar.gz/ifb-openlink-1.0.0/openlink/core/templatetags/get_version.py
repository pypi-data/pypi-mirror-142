from django import template

# from django.conf import settings
from openlink import __version__

register = template.Library()


@register.filter(name="get_version")
def get_version(version):
    return version + __version__
