from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter(name="findCharOrString")
@stringfilter
def findCharOrString(value, arg):
    val = value.find(arg)
    if val == -1:
        return False
    return True