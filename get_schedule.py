import requests
import datetime
from datetime import datetime as dt
import csv
import json
from tabulate import tabulate
from tg_module import send_message
import os.path


def get_schedule_from_url():
    with open("tokens.json", "r") as tokens:
        url = json.load(tokens)["schedule_url"]
        open("schedules/schedule.csv", "wb").write(requests.get(url).content)


def get_schedule(today):
    with open("tokens.json", "r", encoding="utf8") as tokens:
        tokens_loaded = json.load(tokens)
        timezone = datetime.timezone(datetime.timedelta(hours=int(tokens_loaded["timezone_delta"])))
        today_weekday = today.weekday()
        is_even_week = ((dt.now(tz=timezone) - dt(year=2023, month=9, day=4, tzinfo=timezone)).days // 7 + 1) % 2 == 0

        with open('schedules/schedule.csv', newline='', encoding='utf-8') as schedule:
            if today_weekday < 5:
                schedule_reader = [row for row in csv.reader(schedule, delimiter=',')]
                output_schedule = []

                for row_index in range(2 + today_weekday * 12, 14 + today_weekday * 12, 2):
                    lesson_number = schedule_reader[row_index][1]

                    # [2:4] - только для 1 группы
                    row = schedule_reader[row_index + is_even_week][2:4]

                    row[0] = row[0].replace('\n', ' ')
                    if not row[0]: row[0] = '-'
                    if row[0] in tokens_loaded["repeating_lessons"]:
                        row[1] = row[0]

                    row[1] = row[1].replace('\n', ' ')
                    if not row[1]: row[1] = '-'

                    output_schedule.append([lesson_number, row[0], row[1]])

                return tabulate(output_schedule)

            return ""


def send_schedule(today):
    if (today.weekday() == 6) or (not os.path.exists("schedules/schedule.csv")):
        get_schedule_from_url()

    schedule_message = get_schedule(today)

    if schedule_message:
        send_message(schedule_message)