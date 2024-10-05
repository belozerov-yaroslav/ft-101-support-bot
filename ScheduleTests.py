import get_schedule
import datetime as dt


for i in get_schedule.get_schedule(dt.datetime(year=2024, month=10, day=1, tzinfo=dt.timezone(dt.timedelta(hours=5)))):
    print(i)
