from secrets import TG_CHAT_ID, TOKEN
import requests

def send_message(message_text):
    json_params = {"chat_id": TG_CHAT_ID,
                   "text": message_text}
    response_text = requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage",
                                  json=json_params).text
