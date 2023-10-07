from secrets import TG_CHAT_ID, TOKEN
import requests


def send_message(message_text, chat_id=TG_CHAT_ID, turn_on_markdown=False):
    json_params = {"chat_id": chat_id,
                   "text": message_text}
    if turn_on_markdown:
        json_params['parse_mode'] = "MarkdownV2"
    response_text = requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage",
                                  json=json_params).text
