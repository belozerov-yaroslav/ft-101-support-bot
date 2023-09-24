import requests
import datetime
import matan_schedule

def handler(event, context):
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
