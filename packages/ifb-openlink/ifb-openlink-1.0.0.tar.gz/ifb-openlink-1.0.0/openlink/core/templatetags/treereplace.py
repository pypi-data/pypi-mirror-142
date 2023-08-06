from django import template

register = template.Library()


@register.filter(name="treereplace")
def split(
    value,
):
    return value.replace("/", "x2F")
