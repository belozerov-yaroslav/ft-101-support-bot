import os

from tabulate import tabulate
from tg_module import send_message, pin_message, unpin_message
from help_functions import asia_ekat, is_even_week
from ScheduleLoadres import XlsxScheduleLoader
from ObjectStorageWorker import ObjectStorageWorker


def get_pair_name_aud(pair_string : str):
    pair_string = pair_string.replace("\n", ", ")
    pair_name = pair_string.split(",")[0]
    try:
        pair_aud = pair_string.split(",")[1]
    except Exception:
        pair_aud = "-"
    if pair_name == "Математический анализ":
        pair_name = "Матан(Л)"
    elif pair_name == "Алгебра и геометрия":
        if pair_string.find("обуч") == -1:
            pair_name = "Алгем(Л)"
        else:
            pair_name = "Алгем(У)"
    elif pair_name == "Иностранный язык":
        pair_name = "Ин. яз."
    elif pair_name == "Язык  Python":
        pair_name = "Python"
    elif pair_name.startswith("Физкультура"):
        pair_name = "Физра " + pair_name.split()[2]
    elif pair_name.startswith("Основы российской"):
        pair_name = "ОРГ"
    elif pair_name == "Основы продуктового дизайна":
        pair_aud = "-"
        pair_name = "Дизайн"
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
    try:
        pinned_msg_id = ObjectStorageWorker(os.environ.get("OBJECT_STORAGE_BUCKET")).get_object_text("pinned_tg_msg")
        unpin_message(pinned_msg_id)
    except Exception:
        pass

    if schedule_message:
        msg_id = send_message("Расписание на сегодня:")
        ObjectStorageWorker(os.environ.get("OBJECT_STORAGE_BUCKET")).load_object_text(
            os.environ.get("PINNED_TG_MSG_KEY"), str(msg_id))
        send_message(f'`{schedule_message[0]}`', turn_on_markdown=True)
        send_message(f'`{schedule_message[1]}`', turn_on_markdown=True)
        pin_message(str(msg_id))
