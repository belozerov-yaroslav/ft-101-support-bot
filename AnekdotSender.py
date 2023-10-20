import csv
from random import shuffle, choice

import tg_module


def send_anekdot():
    message = "ФИИТовцы! Доброе Утро ❤️\n\n"

    with open('aneks.csv', 'r', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file)
        messages = [row[1] for row in csv_reader]
    shuffle(messages)
    tg_module.send_message(message + choice(messages))


if __name__ == '__main__':
    send_anekdot()
