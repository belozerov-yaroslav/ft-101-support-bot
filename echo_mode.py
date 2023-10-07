from tg_module import send_message
import os


def echo():
    send_message("Function is triggered!", chat_id=os.environ.get("ECHO_CHAT_ID"))
