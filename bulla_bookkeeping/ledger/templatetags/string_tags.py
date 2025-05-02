from django import template

register = template.Library()


@register.filter(name="repeat")
def repeat(string, count):
    """Repeats a string a certain number of times"""
    return string * count
