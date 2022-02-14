from django import template

register = template.Library()


@register.filter(name="listReversed")
def listReversed(value):
    return value[::-1]