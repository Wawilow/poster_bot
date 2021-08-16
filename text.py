import vk_api
from vk_api.bot_longpoll import VkBotLongPoll

from last_post import *

my_token = '7590a1ae275d8b38b843371b2d9c4b64b196df60e43284e50e246f984c22b0f2c3cfe21a159f450d286a2'
bot_token = 'cb0400ae1b14d0875b4803640297401794c9d0984e0585a5521672c3f9aa60e88c856f5ce2248b640ef60'

group_id = 204098688
album_id = 279018273

bot_VK = vk_api.VkApi(token=bot_token)
bot_api = bot_VK.get_api()

user_VK = vk_api.VkApi(token=my_token)
user_api = user_VK.get_api()

bot_longpool = VkBotLongPoll(bot_VK, group_id)


print(f"bot_vk: {type(bot_VK)}")
print(f"bot_api: {type(bot_api)}")
print(f"my_VK: {type(user_VK)}")
print(f"my_api: {type(user_api)}")
print(f"bot_longpool: {type(bot_longpool)}")

print()
print(all_post(user_api, group_id))
