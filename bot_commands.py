from tg_module import send_message


def send_secret_code(message_info):
    send_message("7341#", message_info['chat']['id'])
