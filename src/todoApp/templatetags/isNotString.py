from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter(name="isNotString")
def isNotString(value):
    return not isinstance(value, str)