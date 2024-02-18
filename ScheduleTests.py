import get_schedule
import datetime as dt


for i in get_schedule.get_schedule(dt.datetime(year=2024, month=2, day=15, tzinfo=dt.timezone(dt.timedelta(hours=5)))):
    print(i)