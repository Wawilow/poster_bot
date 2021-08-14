import unittest
from time_convert import *
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll


class Test_unixtime_convert(unittest.TestCase):
    def test_next_post_time(self):
        self.assertEqual()


if __name__ == '__main__':
    global my_api, api, VK, longpoll, token, my_token, group_id, album_id
    my_token = '7590a1ae275d8b38b843371b2d9c4b64b196df60e43284e50e246f984c22b0f2c3cfe21a159f450d286a2'
    token = 'cb0400ae1b14d0875b4803640297401794c9d0984e0585a5521672c3f9aa60e88c856f5ce2248b640ef60'

    group_id = 204098688
    album_id = 279018273
    VK = vk_api.VkApi(token=token)
    longpoll = VkBotLongPoll(VK, group_id)
    api = VK.get_api()
    my_api = (vk_api.VkApi(token=my_token)).get_api()

    print("Server started")
    print(type(VK))
    print(type(group_id))
    print(next_post_time(my_api, group_id))