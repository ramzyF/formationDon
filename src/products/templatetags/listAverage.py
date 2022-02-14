from django import template

register = template.Library()


@register.filter(name="listAverage")
def listAverage(value):
    return  sum(value) / len(value)
