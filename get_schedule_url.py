import requests
import json

def get_schedule_url():
    with open("tokens.json", "r") as tokens:
        url = json.load(tokens)["schedule_url"]
        open("schedules/schedule.csv", "wb").write(requests.get(url).content)