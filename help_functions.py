import datetime as dt

asia_ekat = dt.timezone(dt.timedelta(hours=5))


def is_even_week(today):
    return ((today - dt.datetime(year=2023, month=9, day=4, tzinfo=asia_ekat)).days // 7 + 1) % 2 == 0
