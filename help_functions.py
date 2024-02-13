import datetime as dt

asia_ekat = dt.timezone(dt.timedelta(hours=5))


def is_even_week(today):
    return ((today - dt.datetime(year=2024, month=10, day=12, tzinfo=asia_ekat)).days // 7) % 2 == 0
