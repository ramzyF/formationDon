from django import template

register = template.Library()


@register.filter(name="listMax")
def listMax(value):
    return max(value)