from django import template

register = template.Library()


@register.filter(name="plurals")
def plurals(type):
    return type.get_plural()
