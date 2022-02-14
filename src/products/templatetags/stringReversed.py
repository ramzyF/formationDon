from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter(name="stringReversed")
@stringfilter
def stringReversed(value):
    return value[::-1]