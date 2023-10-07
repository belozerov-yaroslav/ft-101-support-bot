from random import choice
from tg_module import send_message
from lists import BIRTHDAY_LIST, STUDENT_LIST


def checkBirthday(today):
    yearOfBirthdayBoys = []
    surnameNameID = []

    for i in range(len(BIRTHDAY_LIST)):
        if BIRTHDAY_LIST[i][0] == today.day and BIRTHDAY_LIST[i][1] == today.month:
            yearOfBirthdayBoys.append(BIRTHDAY_LIST[i][2])
            surnameNameID.append(STUDENT_LIST[i][0] + ' ' + STUDENT_LIST[i][1] + ' ' + STUDENT_LIST[i][2])

    if len(yearOfBirthdayBoys) == 1:
        message = f"{choice('👏🌞🌻🌼')} Доброе утро, лисята {choice('😍🥰😘')}\n\nCегодня день рождения празднует {surnameNameID[0]}\n\nПоздравляем тебя с {str(today.year - yearOfBirthdayBoys[0])}-летием !!!\nОт всей группы ФТ-101 и кураторов желаем счастья, прогресса и хорошего кода 😍😍😍"
        send_message(message)

    if len(yearOfBirthdayBoys) >= 2:
        message = f"{choice('👏🌞🌻🌼')} Доброе утро, лисята {choice('😍🥰😘')}" + '\n\n' + f"Cегодня день рождения празднуют:" + '\n'
        j = 0
        for i in yearOfBirthdayBoys:
            message += surnameNameID[j] + ' (' + str(today.year - i) + ' лет)\n'
            j += 1

        message += "\nОт всей группы ФТ-101 и кураторов желаем счастья, прогресса и хорошего кода нашим именниникам 😍😍😍"
        send_message(message)
