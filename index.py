import requests
import datetime
from matan_schedule import send_matan_schedule
import echo_mode
from checkBirthday import checkBirthday
from lists import asia_ekat

def handler(event, context):
    today = datetime.datetime.now(tz=asia_ekat)
    echo_mode.echo() # просто отправляет в тг сообщение, что бот жив
    if 'httpMethod' in event.keys() and len(event['queryStringParameters']) == 3:
        parametrs = event['queryStringParameters']
        today = datetime.datetime(day=int(parametrs['day']),
                                  month=int(parametrs['month']),
                                  year=int(parametrs['year']),
                                  tzinfo=asia_ekat)
    send_matan_schedule(today)
    checkBirthday(today)
    return {
        'statusCode': 200,
        'body': 'ok!',
    }
