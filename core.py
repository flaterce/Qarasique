import vk
import time
import importlib


def get_peer_id(message):
    try:
        chat_id = message['chat_id']
        return 2000000000 + chat_id
    except:
        return message['user_id']

token = ''
session = vk.Session(access_token=token)
api = vk.API(session)

last_read_id = -1

while True:
    message = api.messages.get(count=1, out=1)['items'][0]
    time.sleep(1)
    if last_read_id == message['id']:
        continue
    last_read_id = message['id']
    if len(message['body']) != 0 and message['body'][0] == '@':
        text = message['body'].split()
        comm = text[0][1:]
        text.pop(0)
        args = text

        comm_module = importlib.import_module('comms.' + comm)
        comm_module.execute(args, message, api)
