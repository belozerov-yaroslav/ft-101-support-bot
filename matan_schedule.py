from datetime import datetime as dt
from random import choice
from tg_module import send_message
from lists import STUDENT_LIST
from help_functions import asia_ekat, is_even_week


def send_matan_schedule(today):
    week_num = (today - dt(year=2023, month=9, day=25, tzinfo=asia_ekat)).days // 7

    if today.weekday() == 2 or (today.weekday() == 4 and not is_even_week(today)) and week_num <= 13:
        send_message(f"{choice('👏🌞🌻🌼')} Доброе утро, лисята" + ", сегодня МАТАН" +
                     f" {choice('😍🥰😘')}, и сегодня моет доску - {STUDENT_LIST[week_num][0]} {STUDENT_LIST[week_num][1]} {STUDENT_LIST[week_num][2]}")
