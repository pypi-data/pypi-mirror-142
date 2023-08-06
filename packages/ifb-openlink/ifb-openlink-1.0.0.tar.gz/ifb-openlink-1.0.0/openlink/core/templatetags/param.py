from django import template

register = template.Library()


@register.filter(name="param")
def related_param(obj, key):
    return obj.get_param(key)
