# random
from random import randrange

# vk_api
import vk_api
from vk_api.upload import VkUpload

# time convert
from time_convert import for_vk_post_convert
from time_convert import time_now, unixtime_convert

#last post
from last_post import last_postponed_post


def post_make(my_token, group_id='204098688', text='#АдекватныеМемы'):
    Vk_api = vk_api.VkApi(token=my_token)
    VK = Vk_api.get_api()
    new_texts_post(VK, group_id, f'{text}',
                    data=unixtime_convert(time_to_post(
                        time=[*str(last_postponed_post(VK, group_id)).split(' ')[0].split('-'),
                              *str(last_postponed_post(VK, group_id)).split(' ')[1].split(':')], fall=True)))


def new_texts_post(VK, groupId, textPost, data=for_vk_post_convert()):
    attachments = []
    params = {"owner_id": f'-{groupId}', "message": textPost, "attachments": attachments, 'publish_date': data}
    VK.wall.post(**params)


def new_image_post(VK, my_token, groupId, time_to_post, img, text='#АдекватныеМемы', albomId=279018273):
    print(time_to_post)
    my_VK = vk_api.VkApi(token=my_token)
    my_VK = my_VK.get_api()
    upload = VkUpload(my_VK)
    photo = upload.photo(str(img), albomId)
    owner_id = photo[0]['owner_id']
    photo_id = photo[0]['id']
    attachments = f'photo{owner_id}_{photo_id}'
    params = {"owner_id": f'-{groupId}', "message": text, "publish_date": time_to_post,
              "attachments": attachments}
    return f"Номер поста: {my_VK.wall.post(**params)['post_id']}\nИнформация о посте"


def time_to_post(time, small=False, fall=False):
    time = [int(float(i)) for i in time]
    print(time)
    if time == ['[False,', "'no"]:
        time = time_now()
    if not small:
        flag = False
        timing = [4, 7, 12, 15, 17, 20, 22]
        hour = time[3]
        rang = [[0, 5, 1], [6, 10, 2], [11, 13, 3], [14, 16, 4], [17, 18, 5], [19, 21, 6], [22, 24, 0]]
        for i in rang:
            if i[0] <= int(hour) <= i[1]:
                n_hour = timing[i[2]]
                if timing[i[2]] == timing[0]:
                    flag = True
        if flag:
            time[3] = n_hour
            return one_day_plus_time(time)
        else:
            time[3] = n_hour
            return one_day_plus_time(time, delta=0)
    else:
        hour = time[3]
        small_timing = [4, 7, 15, 19, 22]
        rang = [[0, 5, 1], [6, 12, 2], [13, 17, 3], [18, 20, 4], [21, 23, 0]]
        for i in rang:
            if i[0] <= int(hour) <= i[1]:
                n_hour = small_timing[i[2]]
                if small_timing[i[2]] == small_timing[0]:
                    flag = True
        if flag:
            time[3] = n_hour
            return one_day_plus_time(time)
        else:
            time[3] = n_hour
            return one_day_plus_time(time, delta=0)


if __name__ == '__main__':
    my_token = '7590a1ae275d8b38b843371b2d9c4b64b196df60e43284e50e246f984c22b0f2c3cfe21a159f450d286a2'
    bot_token = 'cb0400ae1b14d0875b4803640297401794c9d0984e0585a5521672c3f9aa60e88c856f5ce2248b640ef60'

    group_id = 204098688
    album_id = 279018273

    bot_VK = vk_api.VkApi(token=bot_token)
    bot_api = bot_VK.get_api()

    user_VK = vk_api.VkApi(token=my_token)
    user_api = user_VK.get_api()

