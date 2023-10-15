import requests
import os
import json


def send_message(message_text, chat_id=os.environ.get('TG_CHAT_ID'), turn_on_markdown=False):
    json_params = {"chat_id": chat_id,
                   "text": message_text}
    if turn_on_markdown:
        json_params['parse_mode'] = "MarkdownV2"
    response = requests.post(f"https://api.telegram.org/bot{os.environ.get('TG_TOKEN')}/sendMessage",
                             json=json_params)
    if response.status_code != 200:
        raise Exception
    return json.loads(response.text)["result"]["message_id"]


def pin_message(message_id, chat_id=os.environ.get("TG_CHAT_ID")):
    json_params = {"message_id": message_id,
                   "chat_id": chat_id,
                   "disable_notification": True}
    response = requests.post(f"https://api.telegram.org/bot{os.environ.get('TG_TOKEN')}/pinChatMessage",
                             json=json_params)


def unpin_message(message_id, chat_id=os.environ.get("TG_CHAT_ID")):
    json_params = {"message_id": message_id,
                   "chat_id": chat_id}
    response = requests.post(f"https://api.telegram.org/bot{os.environ.get('TG_TOKEN')}/unpinChatMessage",
                             json=json_params)


if __name__ == '__main__':
    print(send_message("lol", chat_id="-4034505153"))
