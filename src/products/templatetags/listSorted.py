from django import template

register = template.Library()


@register.filter(name="listSorted")
def listSorted(value):
    value.sort()
    return value
