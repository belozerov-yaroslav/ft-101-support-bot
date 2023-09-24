from datetime import datetime as dt
from random import choice
from tg_module import send_message
from lists import STUDENT_LIST, today, asia_ekat

def send_matan_schedule():
    is_even_week = ((today - dt(year=2023, month=9, day=4, tzinfo=asia_ekat)).days // 7 + 1) % 2 == 0
    week_num = (today - dt(year=2023, month=9, day=25, tzinfo=asia_ekat)).days // 7

    if today.weekday() == 2 or (today.weekday() == 4 and not is_even_week) and week_num <= 13:
        send_message(f"{choice('👏🌞🌻🌼')} Доброе утро, лисята" + ", сегодня МАТАН" +
                     f" {choice('😍🥰😘')}, и сегодня моет доску - {STUDENT_LIST[week_num]}")
