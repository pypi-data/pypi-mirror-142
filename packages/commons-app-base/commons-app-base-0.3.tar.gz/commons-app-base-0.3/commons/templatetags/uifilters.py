from commons.python.core.help import format
from django import template
import datetime

register = template.Library()


@register.filter(name='uidecimal')
def format_decimal(val, decimal_places=2):
    return format.format_decimal(val, decimal_places)


@register.filter(name='uicurrency')
def format_currency(val):
    return format.price_format(val)


@register.filter(name='uidate')
def date_format(date: datetime):
    return format.date_format(date)


@register.filter(name='uicapitalize')
def capitalize(value: str):
    return value.capitalize()
