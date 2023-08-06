from django import template

register = template.Library()


@register.filter(name="dict")
def dict(instance):
    return instance.__dict__
