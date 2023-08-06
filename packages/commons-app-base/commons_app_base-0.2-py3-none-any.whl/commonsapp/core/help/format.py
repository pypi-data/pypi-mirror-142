from datetime import date, datetime


def format_decimal(val, decimal_places):
    if isinstance(val, (int, float)):
        return round(val, decimal_places)
    return 0


def price_format(val):
    return f'R$ {val:.2f}'.replace('.', ',')


# TODO implements date format
def date_format(date: date):
    return date.strftime('%d/%m/%Y')


def date_time_format(date_time: datetime):
    return date_time.strftime('%d/%m/%Y %H:%M')
