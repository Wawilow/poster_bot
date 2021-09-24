# vk_api
import vk_api
from vk_api import VkApi
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

# tg
from vk_api.longpoll import VkLongPoll, VkEventType

# time.sleep
from time import sleep

# ast
# this is a analog json. I use ast because json cant work with json file
import ast


# multi task
import multitasking


# my file
from bot_work import *
from data_base import *
from last_post import *
from new_post import *
from time_convert import *
from work_with_photo import *


from icecream import ic
# print = ic

# multitasking for telegram and vk bot
multitasking.set_max_threads(2)
@multitasking.task
def multi_task_vk():
    try:
        print("тут работает вк бот")
        vk_bot()
    except:
        print('вк упал')


multitasking.set_max_threads(2)
@multitasking.task
def multi_task_telegram():
    try:
        print('тут работает телега')
        telegram_bot()
    except:
        return 'телега упала'


# this class get platform + command(already processed) and return answer
class Bot:
    def __init__(self, platform):
        if platform == 'telegram':
            self.platform = 'tg'
            print("Создан объект telegram бота!")
        elif platform == 'vk':
            self.platform = 'vk'
            print(f"Создан объект vk бота")

    def set_user_id(self, user_id):
        self.user_id = user_id
        if self.user_id:
            return True
        else:
            return False

    def set_event(self, event):
        self.event = event
        if self.event:
            return True
        else:
            return False

    def set_user_message(self, message):
        self.message = message
        if message:
            return True
        else:
            return False

    def set_attachments(self, attachments):
        attachments = ast.literal_eval(str(attachments))
        self.attachments = attachments['message']['attachments']
        if attachments:
            return True
        else:
            return False

    def set_attachment(self, attachment):
        self.attachment = attachment
        if attachment:
            return True
        else:
            return False

    def set_download_photo_flag(self, flag):
        self.download_photo = flag

    def get_back(self,
                 user_id=False, event=False, message=False, attachments=False, attachment=False, download_photo=False):
        if user_id:
            return self.user_id
        if event:
            return self.event
        if message:
            return self.message
        if attachments:
            return self.attachments
        if attachment:
            return self.attachment
        if download_photo:
            return self.download_photo

    def get_back_user_id(self):
        return self.user_id

    def get_back_event(self):
        return self.event

    def get_back_message(self):
        return self.message

    def get_back_attachments(self):
        return self.attachments

    def get_back_attachment(self):
        return self.attachment

    def get_back_download_photo(self):
        return self.download_photo

    def message_feedback(self):
        return f'Message for me by: {self.user_id}\nwith text {self.message}'

    def post_photo(self):
        photo = self.attachment['photo']
        url = photo['sizes'][-1]['url']
        # download photo in data base and sand result message
        print(write_msg(self.user_id, bot_api, download_message_image(url, user_id=self.user_id)))
        # download again photo in main folder with name image
        print((download_image_to_post(url, photo_name='image')))
        download_photo = True
        if self.message == '' and self.user_id in [503409544, 239248195]:
            # here i need RUN function write_msg_with_photo, and postponed post
            write_msg(self.user_id, bot_api, (new_image_post(user_token, user_api, group_id, unix_time_convert(my_group_time(user_api, group_id)), "#АдекватныеМемы", 'image.png')))
            # sleep(15)


def my_group_time(user_api, group_id):
    last_p = data_time_convert(last_postponed_post_date(user_api, group_id), delta_hours=3)
    timetopost = time_to_post([last_p.hour, last_p.minute], [[4, 11], [7, 11], [10, 4], [14, 13], [16, 42], [18, 34], [20, 11], [22, 17]])
    if timetopost[0] == True:
        last_p = data_time_convert(last_p, delta_days=1)
        time = datetime.datetime(last_p.year, last_p.month, last_p.day, timetopost[1][0], timetopost[1][1], 0)
    else:
        time = datetime.datetime(last_p.year, last_p.month, last_p.day, timetopost[1][0], timetopost[1][1], 0)
    return time


def vk_bot():
    # run to the event long pool
    for event in bot_longpool.listen():
        # if event is a message
        if event.type == VkBotEventType.MESSAGE_NEW:
            # make bot variable
            bot = Bot("vk")
            # -
            # set download photo flag
            bot.set_download_photo_flag(flag=False)
            # -
            # set user id and event
            bot.set_user_id(user_id=event.object['message']['from_id'])
            bot.set_event(event=event)
            # -
            # set message text
            bot.set_user_message(message=event.object['message']['text'])
            # -
            # print about message
            print(bot.message_feedback())

            # if we have something file in message
            if bot.set_attachments(attachments=event.object):
                # run in the message
                for attachment in bot.get_back_attachments():
                    # if in message have photo
                    bot.set_attachment(attachment)
                    if bot.get_back_attachment()['type'] == 'photo':
                        bot.post_photo()


def telegram_bot():
    token = 'f626cee422e9d40baf72cdb457b391a82fe1ba7a8cb5968be52f4094504a2ddedc4df00cf098ad5bdb454'
    vk = vk_api.VkApi(token=token)
    api = vk.get_api()
    longpoll = VkLongPoll(vk)
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            if event.to_me:
                print('message')


# set my variables, after hee all be get from sql table
def main():
    global user_token, bot_token

    global group_id, album_id

    global bot_VK, bot_api

    global user_VK, user_api

    global bot_longpool

    user_token = '7590a1ae275d8b38b843371b2d9c4b64b196df60e43284e50e246f984c22b0f2c3cfe21a159f450d286a2'
    bot_token = 'cb0400ae1b14d0875b4803640297401794c9d0984e0585a5521672c3f9aa60e88c856f5ce2248b640ef60'

    # group_id = 204098688
    bot_group_id = 204098688
    group_id = 198242788
    album_id = 279018273

    bot_VK = vk_api.VkApi(token=bot_token)
    bot_api = bot_VK.get_api()

    user_VK = vk_api.VkApi(token=user_token)
    user_api = user_VK.get_api()

    bot_longpool = VkBotLongPoll(bot_VK, bot_group_id)

    print("Server started")


if __name__ == '__main__':
    # set initial values
    main()
    # run to the event long pool vk
    multi_task_vk()
    # run to the event long pool telegram
    multi_task_telegram()

