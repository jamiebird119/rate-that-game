from datetime import date, timedelta
from django import template


register = template.Library()


@register.filter(name='format_date')
def format_date(date, tag):
    if type(date) == 'str':
        date = date.strptime("%Y %m %d")
    else:
        date = date
    if tag == 'SHORT':
        date_new = date.strftime('%b %d')
    elif tag == 'HEADER':
        date_new = date.strftime('%A %d %b')
    elif tag == "SEARCH":
        date_new = date.strftime("%Y/%d/%m")
    return date_new


@register.filter(name="percentage")
def percentage(perc):
    value = round(perc*100)
    return value
