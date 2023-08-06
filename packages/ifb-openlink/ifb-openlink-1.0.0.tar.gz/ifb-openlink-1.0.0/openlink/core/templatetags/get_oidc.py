from django import template
from django.conf import settings

register = template.Library()


@register.filter(name="get_oidc")
def get_oidc(val=None):
    return settings.AUTH_OIDC
