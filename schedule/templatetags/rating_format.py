from django import template

register = template.Library()


@register.filter(name='format_rating')
def format_rating(rating):
    return round(rating*2)/2
