from django import template


register = template.Library()


@register.filter(name="adder")
def adder(value, arg):
    return value + arg