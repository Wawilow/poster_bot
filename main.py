# vk_api
import vk_api
from vk_api import VkApi
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

# time.sleep
from time import sleep

# ast
# this is a analog json. I use ast because json cant work with json file
import ast


from icecream import ic
# print = ic


class Bot:
    def __init__(self, user_id):
        print("\nСоздан объект бота!")

        self._USER_ID = user_id
        begin = ['GO', 'НАЧАТЬ', 'ПОГНАЛИ', 'ПОЕХАЛИ', 'СТАРТ', 'ГО']
        good_bye = ['GOOD BAY', 'ПОКА']
        self._COMMANDS = [begin, good_bye]

    def new_message(self, user_id, message):
        if message.upper() in self._COMMANDS[0]:#начать
            return f'Зачем?'
        elif message.upper() in self._COMMANDS[1]:#stop
            return f'абоба'
        else:
            return f'У меня нету этой команды, если ты хочешь узнать список команд напиши «help»'


class Image:
    def __init__(self, event, user_id, message, atchs, atch, group_id, VK, my_api):
        print("\nПрислали фото")
        self.event, self.user_id, self.message, self.atchs, self.atch, self.group_id, self.VK, self.my_api\
            = event, user_id, message, atchs, atch, group_id, VK, my_api


    def image(self):
        event, user_id, message, atchs, atch, group_id, VK, my_api =\
            self.event, self.user_id, self.message, self.atchs, self.atch, self.group_id, self.VK, self.my_api
        photo = atch['photo']
        url = photo['sizes'][-1]['url']
        # download photo in data base and sand result message
        print(write_msg(user_id, api,
                        download_message_image(url, user_id=user_id)))
        # download again photo in main folder with name image
        print((download_image_to_post(url, photo_name='image')))
        if message == '' and user_id == 503409544:
            # here i need RUN function write_msg_with_photo, and postponed post
            self.event, self.user_id, self.message, self.atchs, self.atch, self.group_id, self.VK, self.my_api \
                = event, user_id, message, atchs, atch, group_id, VK, my_api
            return [user_id, my_api,
                      (new_image_post(VK, my_token, group_id,
                                      (unixtime_convert(time_to_post(
                                          str(last_postponed_post(my_api, group_id)).split(' ')[0].split('-') +
                                          str(last_postponed_post(my_api, group_id)).split(' ')[1].split(':')))),
                                      img='image.png', albomId=album_id))]


def main():
    global user_token, bot_token, group_id, album_id
    global bot_VK, bot_api, user_VK, user_api
    global bot_longpool

    user_token = '7590a1ae275d8b38b843371b2d9c4b64b196df60e43284e50e246f984c22b0f2c3cfe21a159f450d286a2'
    bot_token = 'cb0400ae1b14d0875b4803640297401794c9d0984e0585a5521672c3f9aa60e88c856f5ce2248b640ef60'

    group_id = 204098688
    album_id = 279018273

    bot_VK = vk_api.VkApi(token=bot_token)
    bot_api = bot_VK.get_api()

    user_VK = vk_api.VkApi(token=user_token)
    user_api = user_VK.get_api()

    bot_longpool = VkBotLongPoll(bot_VK, group_id)

    print("Server started")


if __name__ == '__main__':
    # set initial values
    main()
