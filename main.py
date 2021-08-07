# vk_api
import vk_api
from vk_api import VkApi
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

# random
from random import randrange

# program file
from new_post import write_msg
from time_convert import unixtime_convert
from last_post import last_postponed_post
from work_with_photo import download_message_image, download_image_to_post

# ast
# this is a analog json. I use ast because json cant work with json file
import ast

from icecream import ic
# print = ic


class Test_Bot:
    def __init__(self, user_id):
        print("\nСоздан объект бота!")

        self._USER_ID = user_id
        begin = ['GO', 'НАЧАТЬ', 'ПОГНАЛИ', 'ПОЕХАЛИ', 'СТАРТ', 'ГО']
        good_bye = ['GOOD BAY', 'ПОКА']
        self._COMMANDS = [begin, good_bye]

    def new_message(self, message, user_id):
        if message.upper() in self._COMMANDS[0]:#начать
            return f'Зачем?'
        elif message.upper() in self._COMMANDS[3]:#stop
            return f'абоба'
        else:
            # print(message, self._COMMANDS[1], message.lower() == self._COMMANDS[1])
            return f'У меня нету этой команды, если ты хочешь узнать список команд напиши «help»'


def main():
    global api, vk, longpoll
    main_token = '7590a1ae275d8b38b843371b2d9c4b64b196df60e43284e50e246f984c22b0f2c3cfe21a159f450d286a2'
    token = 'cb0400ae1b14d0875b4803640297401794c9d0984e0585a5521672c3f9aa60e88c856f5ce2248b640ef60'

    vk = vk_api.VkApi(token=token)
    longpoll = VkBotLongPoll(vk, 204098688)
    api = vk.get_api()

    print("Server started")


if __name__ == '__main__':
    main()
    while True:
        for event in longpoll.listen():
            if event.type == VkBotEventType.MESSAGE_NEW:
                atchs = event.object
                if atchs:
                    atchs = ast.literal_eval(str(atchs))
                    atchs = atchs['message']['attachments']
                    for atch in atchs:
                        if atch['type'] == 'photo':
                            photo = atch['photo']
                            url = photo['sizes'][-1]['url']
                            print(write_msg(atch['photo']['owner_id'],
                                            download_message_image(url, user_id=atch['photo']['owner_id'])))
                            # print(write_msg(atch['photo']['owner_id'],))
                            print((download_image_to_post(url, photo_name='image')))
                    print()
                    print('New message:')

