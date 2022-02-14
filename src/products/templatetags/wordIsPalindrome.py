from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter(name="wordIsPalindrom")

def wordIsPalindrom(value):
    return value == value[::-1]#exple: été....