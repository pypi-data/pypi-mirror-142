from django import template

register = template.Library()


@register.filter(name="plurals_type")
def plurals_type(type):
    plural_form = {
        "investigation": "investigations",
        "study": "studies",
        "assay": "assays",
        "dataset": "datasets",
        "folder": "folders",
        "experiment": "experiments",
    }

    return plural_form[type]
