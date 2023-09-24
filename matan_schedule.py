import requests
from datetime import datetime as dt
import datetime
from datetime import timedelta
from random import choice
from tg_module import send_message

STUDENT_LIST = ['Ахматнуров Артём @Mot1xx',
                'Балин Арсений @dabbler_0',
                'Батин Андрей @Duxar1',
                'Белозеров Ярослав @yarbely',
                'Бутовой Владислав @eseerli',
                'Горбунов Сергей @fomidon',
                'Гордеев Александр @sandergord',
                'Ибрагимов Дени @den_ibr',
                'Иванов Антон @antonchik300',
                'Коршунов Павел @pashaKors',
                'Костарева Анастасия @nastyakostt',
                'Костромина Алина @llladddy',
                'Кускова Евгения @kuskova_z',
                'Лагутин Денис @Bu16a']

asia_ekat = datetime.timezone(timedelta(hours=5)) # на сервере время UTC+0

def send_matan_schedule(today=None):
    if today is None:
        today = dt.now(tz=asia_ekat) # везде используем today,
    # чтобы для тестирования просто менять today, а не крутить дату в системе
    is_even_week = ((today - dt(year=2023, month=9, day=4, tzinfo=asia_ekat)).days // 7 + 1) % 2 == 0
    if today.weekday() == 2 or (today.weekday() == 4 and not is_even_week):
        week_num = (today - dt(year=2023, month=9, day=25, tzinfo=asia_ekat)).days // 7
        print(week_num)
        send_message(f"{choice('👏🌞🌻🌼')} Доброе утро, лисята, сегодня МАТАН" +
                     f" {choice('😍🥰😘')}, и сегодня моет доску - {STUDENT_LIST[week_num]}")
