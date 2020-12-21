from datetime import date, timedelta
from django import template


register = template.Library()


@register.filter(name='format_date')
def format_date(date, tag):
    date = date
    if tag == 'SHORT':
        date_new = date.strftime('%b %d')
    elif tag == 'HEADER':
        date_new = date.strftime('%A %d %b')
    return date_new
