# vk_api
import vk_api
from vk_api import VkApi
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

# random
from random import randrange

# program file
from new_post import time_to_post, new_texts_post
from time_convert import unixtime_convert
from last_post import last_postponed_post
from work_with_photo import download_message_image

# ast
# this is a analog json. I use ast because json cant work with json file
import ast

from icecream import ic
# print = ic

def post_make(groupId='204098688', text='\n'):
    main_token = 'ad135a8d6e65aa945e86f32aa44e9fd8f5ce4977a18a8b85a12ac9b3079c991c46699611ff17e7679bff6'
    vk_api = VkApi(token=main_token)
    VK = vk_api.get_api()
    new_texts_post(VK, groupId,
                    '#АдекватныеМемы',
                    data=unixtime_convert(time_to_post(
                        time=[*str(last_postponed_post(VK, groupId)).split(' ')[0].split('-'),
                              *str(last_postponed_post(VK, groupId)).split(' ')[1].split(':')], fall=True))
                    )


def write_msg(user_id, message, phhoto):
    if message == 'Готово':
        write_msg_with_photo(user_id, message, phhoto)
    else:
        api.messages.send(user_id=user_id, message=str(message), random_id=randrange(999999999))


def write_msg_with_photo(user_id, message, phhoto):
    upload = vk_api.VkUpload(vk)
    photo = upload.photo_messages(str(phhoto))
    owner_id = photo[0]['owner_id']
    photo_id = photo[0]['id']
    access_key = photo[0]['access_key']
    attachment = f'photo{owner_id}_{photo_id}_{access_key}'
    api.messages.send(user_id=user_id, message=str(message), random_id=randrange(999999999),
                      attachment=attachment)


class Test_Bot:
    def __init__(self, user_id):
        print("\nСоздан объект бота!")

        self._USER_ID = user_id
        begin = ['GO', 'НАЧАТЬ', 'ПОГНАЛИ', 'ПОЕХАЛИ', 'СТАРТ', 'ГО']
        help = ['HELP', 'ПОМОГИ', 'ПОМОЩ', 'ЧЕГО БЛЯТЬ', 'КОМАНДЫ']
        stop = ['STOP', 'СТОП', 'АСТАНОВИСЬ']
        good_bye = ['GOOD BAY', 'ПОКА']
        self._COMMANDS = [begin, help, stop, good_bye]

    def new_message(self, message, user_id):
        if message.upper() in self._COMMANDS[0]:#начать
            return f'Выберити шаблон \n {all_shab_text}'
        elif message.upper() in self._COMMANDS[1]:#help
            return f'\n{all_comands}'
        elif message.upper() in self._COMMANDS[2]:#stop
            del hu_make[user_id]
            return f'Все шаблоны очищены'
        elif message.upper() in self._COMMANDS[3]:#stop
            return f'абоба'
        else:
            # print(message, self._COMMANDS[1], message.lower() == self._COMMANDS[1])
            return f'У меня нету этой команды, если ты хочешь узнать список команд напиши «help»'


def main():
    global api, vk, longpoll
    hu_make = {}
    # 1538369a1ae2c6f51c0bcb22c7a2c1444209b4610a30d33319baea3f59dc975e6d902e28f8d2fa2836818
    token = 'cb0400ae1b14d0875b4803640297401794c9d0984e0585a5521672c3f9aa60e88c856f5ce2248b640ef60'

    vk = vk_api.VkApi(token=token)
    longpoll = VkBotLongPoll(vk, 204098688)
    api = vk.get_api()

    print("Server started")


def name_from_id(a):
    return a


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
                            print(download_message_image(url, 'photo_name'))
                            # print([i for i in f])
                    print()
                    print('New message:')

