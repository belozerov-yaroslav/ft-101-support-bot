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
                'Гальянов Фёдор @Snxws993',
                'Горбунов Сергей @fomidon',
                'Гордеев Александр @sandergord',
                'Ибрагимов Дени @den_ibr',
                'Иванов Антон @antonchik300',
                'Коршунов Павел @pashaKors',
                'Костарева Анастасия @nastyakostt',
                'Костромина Алина @llladddy',
                'Кускова Евгения @kuskova_z',
                'Лагутин Денис @Bu16a',
                'Ловыгин Максим @Minetoff',
                'Маликов Роберт @BaaRobert',
                'Михренин Роман @fok_u',
                'Мордвичев Сергей @echpokus',
                'Овчинников Кирилл @OK916',
                'Орныш Якоб @jakobsw1ft',
                'Спицын Егор @Kkeie',
                'Старцев Кирилл @Serpentg5',
                'Токписев Дмитрий @lyub_dim',
                'Трусов Алексей @LexaSleep',
                'Ульмаскулов Илья @iloveparizh',
                'Шаравьев Артем @trueforme',
                'Шихова Елизавета @ElizavetaShikhova',
                ]

BIRTHDAY_LIST = [[14, 7, 2005], [21, 6, 2005], [22, 10, 2005], [11, 1, 2005],
                 [3, 4, 2006], [28, 5, 2004], [25, 3, 2005], [13, 12, 2005], [29, 11, 2005],
                 [18, 11, 2006], [7, 7, 2005], [8, 8, 2005], [23, 11, 2004],
                 [2, 4, 2004], [28, 7, 2005], [1, 5, 2005], [5, 10, 2005],
                 [25, 3, 2005], [3, 1, 2006], [24, 4, 2005], [3, 2, 2006],
                 [16, 3, 2005], [4, 7, 2005], [25, 6, 2005], [21, 4, 2005],
                 [22, 3, 2005], [6, 1, 2005], [12, 1, 2006]]

asia_ekat = datetime.timezone(timedelta(hours=5))  # на сервере время UTC+0


def send_matan_schedule(today=None):
    if today is None:
        today = dt.now(tz=asia_ekat)  # везде используем today,
        # чтобы для тестирования просто менять today, а не крутить дату в системе

    is_even_week = ((today - dt(year=2023, month=9, day=4, tzinfo=asia_ekat)).days // 7 + 1) % 2 == 0
    week_num = (today - dt(year=2023, month=9, day=25, tzinfo=asia_ekat)).days // 7
    countBirthdayBoys2004 = BIRTHDAY_LIST.count([today.day, today.month, 2004])
    countBirthdayBoys2005 = BIRTHDAY_LIST.count([today.day, today.month, 2005])
    countBirthdayBoys2006 = BIRTHDAY_LIST.count([today.day, today.month, 2006])
    countAllBirthdayBoys = countBirthdayBoys2004 + countBirthdayBoys2005 + countBirthdayBoys2006

    if today.weekday() == 2 or (today.weekday() == 4 and not is_even_week) and week_num <= 13:
        send_message(f"{choice('👏🌞🌻🌼')} Доброе утро, лисята" + ", сегодня МАТАН" +
                     f" {choice('😍🥰😘')}, и сегодня моет доску - {STUDENT_LIST[week_num]}")
    if countAllBirthdayBoys == 1:
        indexBirthdayBoy = BIRTHDAY_LIST.index([today.day, today.month, 2005])
        send_message(f"{choice('👏🌞🌻🌼')} Доброе утро, лисята {choice('😍🥰😘')}" + '\n\n' +
                     f"Cегодня день рождения празднует {STUDENT_LIST[indexBirthdayBoy]}" + '\n\n' +
                     "Поздравляем тебя с " +
                     str(today.year - BIRTHDAY_LIST[indexBirthdayBoy][2]) + "-летием!!!" + '\n' +
                     "От всей группы ФТ-101 и кураторов желаем счастья, прогресса и хорошего кода 😍😍😍")
    if countAllBirthdayBoys >= 2:

        indexesBirthdayBoys = []
        startIndex = 0
        for i in range(countBirthdayBoys2004):
            if i == 0:
                indexesBirthdayBoys.append(
                    BIRTHDAY_LIST.index([today.day, today.month, 2004], startIndex % len(BIRTHDAY_LIST)))
            else:
                indexesBirthdayBoys.append(
                    BIRTHDAY_LIST.index([today.day, today.month, 2004], (startIndex + 1) % len(BIRTHDAY_LIST)))
            startIndex = indexesBirthdayBoys[-1]

        startIndex = 0
        for i in range(countBirthdayBoys2005):
            if i == 0:
                indexesBirthdayBoys.append(
                    BIRTHDAY_LIST.index([today.day, today.month, 2005], startIndex % len(BIRTHDAY_LIST)))
            else:
                indexesBirthdayBoys.append(
                    BIRTHDAY_LIST.index([today.day, today.month, 2005], (startIndex + 1) % len(BIRTHDAY_LIST)))
            startIndex = indexesBirthdayBoys[-1]

        startIndex = 0
        for i in range(countBirthdayBoys2006):
            if i == 0:
                indexesBirthdayBoys.append(
                    BIRTHDAY_LIST.index([today.day, today.month, 2006], startIndex % len(BIRTHDAY_LIST)))
            else:
                indexesBirthdayBoys.append(
                    BIRTHDAY_LIST.index([today.day, today.month, 2006], (startIndex + 1) % len(BIRTHDAY_LIST)))
            startIndex = indexesBirthdayBoys[-1]
        message = f"{choice('👏🌞🌻🌼')} Доброе утро, лисята {choice('😍🥰😘')}" + '\n\n' + f"Cегодня день рождения празднуют:" + '\n'

        for i in indexesBirthdayBoys:
            message += STUDENT_LIST[i] + ' (' + str(today.year - BIRTHDAY_LIST[i][2]) + ' лет)\n'
        message += "\nОт всей группы ФТ-101 и кураторов желаем счастья, прогресса и хорошего кода нашим именниникам 😍😍😍"

        send_message(message)
