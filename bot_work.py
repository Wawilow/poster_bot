from random import randrange

import vk_api


def write_msg(user_id, bot_api, message):
    if type(user_id) != type(1):
        try:
            int(user_id)
        except:
            return f'user id type error'
    if str(type(bot_api)) != "<class 'vk_api.vk_api.VkApiMethod'>":
        return f'bot api type error'
    if type(message) != type('1'):
        try:
            str(message)
        except:
            return f'message type error'
    try:
        return bot_api.messages.send(user_id=user_id, message=str(message), random_id=randrange(999999999))
    except:
        return f'send massage error'


def write_msg_with_photo(bot_VK, bot_api, user_id, message, photo):
    # bot vk
    if str(type(bot_VK)) != "<class 'vk_api.vk_api.VkApi'>":
        return f'bot vk type error'
    # bot api
    if str(type(bot_api)) != "<class 'vk_api.vk_api.VkApiMethod'>":
        return f'bot api type error'
    # user id
    if type(user_id) != type(1):
        try:
            int(user_id)
        except:
            return f'user id type error'
    # message
    if type(message) != type('1'):
        try:
            str(message)
        except:
            return f'message type error'
    try:
        photo = vk_api.VkUpload(bot_VK).photo_messages(str(photo))
    except:
        return 'upload photo error'
    try:
        attachment = f'photo{photo[0]["owner_id"]}_{photo[0]["id"]}_{photo[0]["access_key"]}'
    except:
        return 'configure request error'
    try:
        return bot_api.messages.send(user_id=user_id, message=str(message), random_id=randrange(999999999), attachment=attachment)
    except:
        return 'request error'
