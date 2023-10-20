import os
import datetime
from matan_schedule import send_matan_schedule
import echo_mode
from checkBirthday import checkBirthday
from get_schedule import send_schedule
import json
import bot_commands
import logging
from help_functions import asia_ekat
import AnekdotSender


def handler(event, context):
    try:
        if 'event_metadata' in event.keys():
            triggered_launch(event)
        return http_triggered(event)
    except Exception as e:
        logging.error('Error at %s', exc_info=e)


def triggered_launch(event):
    if event["details"]["trigger_id"] == os.environ.get("ANEK_TRIGGER_ID"):
        return AnekdotSender.send_anekdot()
    return scheduled_launch()


def scheduled_launch(today=datetime.datetime.now(tz=asia_ekat)):
    echo_mode.echo()
    send_matan_schedule(today)
    checkBirthday(today)
    send_schedule(today)
    return {
        'statusCode': 200,
        'body': 'ok!',
    }


def http_triggered(http_data):
    if len(http_data['queryStringParameters']) == 3:
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
