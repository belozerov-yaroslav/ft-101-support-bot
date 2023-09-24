from secrets import ECHO_CHAT
from tg_module import send_message


def echo():
    send_message("Function is triggered!", chat_id=ECHO_CHAT)
    
