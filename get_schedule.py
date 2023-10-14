import requests
import datetime
from datetime import datetime as dt
import csv
import json
from tabulate import tabulate
from tg_module import send_message
import os.path
from help_functions import asia_ekat, is_even_week
from ScheduleLoadres import XlsxScheduleLoader


def get_pair_name_aud(pair_string):
    pair_string = pair_string.split('\n')[0]
    pair_name = pair_string.split(",")[0]
    try:
        pair_aud = pair_string.split(",")[1]
    except Exception:
        pair_aud = "-"
    if pair_name == "Математический анализ":
        pair_name = "Матан(Л)"
    elif pair_name == "Алгебра и геометрия":
        pair_name = "Алгем(Л)"
    elif pair_name == "Иностранный язык":
        pair_name = "Ин. яз."
    elif pair_name.startswith("Физкультура"):
        pair_name = "Физра " + pair_name.split()[1]
    elif pair_name.startswith("Основы российской"):
        pair_name = "ОРГ"
    elif pair_name == "ОПД":
        pair_aud = "-"
    return pair_aud, pair_name


def construct_schedule_message(pair_schedule, pairs, title):
    output_strings = [["", title.split()[0], title.split()[1]]]
    for i in range(len(pairs)):
        if all(map(lambda a: a is None, pairs[i:])):
            break
        if pairs[i] is None:
            output_strings.append([pair_schedule[i], "-"])
            output_strings.append([])
        else:
            output_strings.append([pair_schedule[i], *get_pair_name_aud(pairs[i])])
            output_strings.append([])
    return tabulate(output_strings, headers="firstrow", tablefmt="plain")


def get_schedule(today):
    weekday = today.weekday()
    schedule_loader = XlsxScheduleLoader("schedules/schedule.xlsx", "ФИИТ-1")
    all_pairs = schedule_loader.load()
    first_subgroup_pairs = all_pairs[0][is_even_week(today)][weekday]
    second_subgroup_pairs = all_pairs[1][is_even_week(today)][weekday]
    if all(map(lambda a: a is None, first_subgroup_pairs + second_subgroup_pairs)):
        return None
    f_mes = construct_schedule_message(schedule_loader.load_pair_schedule(), first_subgroup_pairs, "1 подгруппа")
    s_mes = construct_schedule_message(schedule_loader.load_pair_schedule(), second_subgroup_pairs, "2 подгруппа")
    return [f_mes, s_mes]


def send_schedule(today):
    schedule_message = get_schedule(today)

    if schedule_message:
        send_message("Расписание на сегодня:")
        send_message(f'`{schedule_message[0]}`', turn_on_markdown=True)
        send_message(f'`{schedule_message[1]}`', turn_on_markdown=True)
