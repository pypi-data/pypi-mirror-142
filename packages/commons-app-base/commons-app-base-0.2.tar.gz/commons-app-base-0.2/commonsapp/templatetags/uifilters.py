from commonsapp.core.help import format
from django import template
import datetime

register = template.Library()


@register.filter(name='fdecimal')
def format_decimal(val, decimal_places=2):
    return format.format_decimal(val, decimal_places)


@register.filter(name='fcurrency')
def format_currency(val):
    return format.price_format(val)


@register.filter(name='fdate')
def date_format(date: datetime):
    return format.date_format(date)


# TODO implements date-time format
@register.filter(name='fdatetime')
def date_time_format():
    ...
