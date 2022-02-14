from django import template

register = template.Library()


@register.filter(name="listMin")
def listMin(value):
    return min(value)