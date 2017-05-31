import vk
import random

# TEMP
def get_peer_id(message):
    try:
        chat_id = message['chat_id']
        return 2000000000 + chat_id
    except:
        return message['user_id']


def execute(args, message, api):
    answers = [
        'ДА',
        'НЕТ',
        'ЭТО НЕ ВАЖНО',
        'СПОК, БРО',
        'ТОЛСТО',
        'ДА, ХОТЯ ЗРЯ',
        'НИКОГДА',
        '100%',
        '1 из 100',
        'ЕЩЕ РАЗОК'
    ]
    answer = answers[random.randint(0, 9)]

    api.messages.send(peer_id=get_peer_id(message), message=answer)
