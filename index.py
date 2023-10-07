import os

import requests
import datetime
from matan_schedule import send_matan_schedule
import echo_mode
from checkBirthday import checkBirthday
from lists import asia_ekat
from get_schedule import send_schedule
from tg_module import send_message
import json
import bot_commands


def handler(event, context):
    try:
        if 'event_metadata' in event.keys():
            return scheduled_launch()
        return http_triggered(event)
    except Exception as e:
        send_message(str(e), os.environ.get("ECHO_CHAT_ID"))


def scheduled_launch(today=datetime.datetime.now(tz=asia_ekat)):
    echo_mode.echo()
    try:
        send_matan_schedule(today)
    except:
        pass
    try:
        checkBirthday(today)
    except:
        pass
    try:
        send_schedule(today)
    except:
        pass
    return {
        'statusCode': 200,
        'body': 'ok!',
    }


def http_triggered(http_data):
    if len(http_data['queryStringParameters']) == 3 and \
            http_data['queryStringParameters'].keys == ['day', 'month', 'year']:
        parameters = http_data['queryStringParameters']
        today = datetime.datetime(day=int(parameters['day']),
                                  month=int(parameters['month']),
                                  year=int(parameters['year']),
                                  tzinfo=asia_ekat)
        return scheduled_launch(today)
    http_body = json.loads(http_data['body'])
    if 'message' in http_body:
        if http_body['message']['entities'][0]['type'] == 'bot_command':
            try_load_command(http_body['message'])
    return {
        'statusCode': 200,
        'body': 'ok!',
    }


def try_load_command(message_info):
    def check_command(command_text):
        return command == command_text or command == command_text + '@ft_101_support_bot'

    command = message_info['text']
    if check_command('/code'):
        bot_commands.send_secret_code(message_info)
