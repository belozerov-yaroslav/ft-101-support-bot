import requests
import datetime
import matan_schedule
import echo_mode

def handler(event, context):
    echo_mode.echo() # просто отправляет в тг сообщение, что бот жив
    if 'httpMethod' in event.keys() and len(event['queryStringParameters']) == 3:
        parametrs = event['queryStringParameters']
        matan_schedule.send_matan_schedule(datetime.datetime(day=int(parametrs['day']),
                                                             month=int(parametrs['month']),
                                                             year=int(parametrs['year']),
                                                             tzinfo=matan_schedule.asia_ekat))
        return {
            'statusCode': 200,
            'body': 'Testing ok!',
        }
    matan_schedule.send_matan_schedule()
    return {
        'statusCode': 200,
        'body': 'ok!',
    }
