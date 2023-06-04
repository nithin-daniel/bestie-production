from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
@stringfilter
def split(value):
    """Removes all values of arg from the given string"""
    return value.split()

register.filter('split',split)
