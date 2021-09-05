# random
from random import randrange

# vk_api
import vk_api
from vk_api.upload import VkUpload

# time convert
from time_convert import *

#last post
from last_post import *


def my_group_time(user_api, group_id):
    last_p = data_time_convert(last_postponed_post_date(user_api, group_id), delta_hours=3)
    timetopost = time_to_post([last_p.hour, last_p.minute], [[4, 11], [7, 11], [10, 4], [14, 13], [16, 42], [18, 34], [20, 11], [22, 17]])
    if timetopost[0] == True:
        last_p = data_time_convert(last_p, delta_days=1)
        time = datetime.datetime(last_p.year, last_p.month, last_p.day, timetopost[1][0], timetopost[1][1], 0)
    else:
        time = datetime.datetime(last_p.year, last_p.month, last_p.day, timetopost[1][0], timetopost[1][1], 0)
    return time


def post_make(my_token, group_id='204098688', text='#АдекватныеМемы'):
    Vk_api = vk_api.VkApi(token=my_token)
    VK = Vk_api.get_api()
    # new_texts_post(VK, group_id, f'{text}', data=unixtime_convert(time_to_post(time=[*str(last_postponed_post(VK, group_id)).split(' ')[0].split('-'), *str(last_postponed_post(VK, group_id)).split(' ')[1].split(':')], fall=True)))


def new_texts_post(user_api, group_id, text, date):
    # check all variable
    if not (type(user_api) is vk_api.vk_api.VkApiMethod):
        return 'user api type error'
    if not (type(group_id) is int):
        return 'group_id type error'
    try:
        text = str(text)
    except:
        return 'text type error'
    try:
        attachments = []
        params = {"owner_id": f'-{group_id}', "message": text, "attachments": attachments, 'publish_date': date}
        return user_api.wall.post(**params)
    except:
        return 'wall post error'


def new_image_post(user_VK, groupId, albomId, time, text, img):
    try:
        upload = VkUpload(user_VK)
        photo = upload.photo(str(img), albomId)
    except:
        return 'upload error'
    try:
        owner_id = photo[0]['owner_id']
        photo_id = photo[0]['id']
        attachments = f'photo{owner_id}_{photo_id}'
    except:
        return 'get attachments error'
    try:
        params = {"owner_id": f'-{groupId}', "message": text, "publish_date": time, "attachments": attachments}
        return user_VK.wall.post(**params)['post_id']
    except:
        return 'wall post error'


def dumerandwojack_time_to_post(time, small=False, fall=False):
    time = [int(float(i)) for i in time]
    print(time)
    if time == ['[False,', "'no"]:
        time = []
        # time_now()
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
            # return one_day_plus_time(time)
        else:
            time[3] = n_hour
            # return one_day_plus_time(time, delta=0)
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
            # return one_day_plus_time(time)
        else:
            time[3] = n_hour
            # return one_day_plus_time(time, delta=0)


def time_to_post(time, table):
    # check variable time
    # 1) time is list
    # 2) len time is 2
    # 3) all elem in time is int
    # 4) hour is bigger 0 and lower 24, minute is bigger 0 and lower 60
    if type(time) is list:
        if len(time) == 2:
            try:
                time = [int(i) for i in time]
                if not(0 <= time[0] < 24):
                    return 'error hour in time'
                if not(0 <= time[1] < 60):
                    return 'error minute in error'
            except:
                return 'error type elem in time'
        else:
            return 'len time error'
    else:
        return 'time type error'
    # here test table variable
    if type(table) is list:
        check_table = [True for i in table]
        for i in range(len(table)):
            if not (len(table[i]) == 2):
                check_table[i] = False
            try:
                if not (0 <= int(table[i][0]) < 24):
                    check_table[i] = False
                if not (0 <= int(table[i][1]) < 60):
                    check_table[i] = False
            except:
                return 'type in table error'
        if not (all(check_table)):
            return 'table error'
    else:
        return 'type table error'
    # -
    # here i need write function to sort table, if user is too stupid
    # -
    # timing = [7, 20]
    # table = [[7, 30], [7, 50], [11, 0]]
    for i in range(len(table) - 1):
        # -
        # check the time, if it is less than minimum time in table
        if time[0] == table[0][0]:
            # check minute
            if time[1] < table[0][1]:
                return [False, table[0]]
        # check hour
        if time[0] < table[0][0]:
            return [False, table[0]]
        # -
        # check the time, if it is bigger than maximum time
        if time[0] == table[-1][0]:
            # check minute
            if time[1] > table[-1][1]:
                return [True, [table[0]]]
        # check hour
        if time[0] >= table[-1][0]:
            return [True, table[0]]
        # -
        # here go to the list and check next post time
        if table[i][0] == table[i + 1][0]:
            if table[i][1] <= time[1] < table[i + 1][1]:
                return [False, table[i + 1]]
        if table[i][0] <= time[0] < table[i + 1][0]:
            return [False, table[i + 1]]



if __name__ == '__main__':
    my_token = '7590a1ae275d8b38b843371b2d9c4b64b196df60e43284e50e246f984c22b0f2c3cfe21a159f450d286a2'
    bot_token = 'cb0400ae1b14d0875b4803640297401794c9d0984e0585a5521672c3f9aa60e88c856f5ce2248b640ef60'

    group_id = 204098688
    album_id = 279018273

    bot_VK = vk_api.VkApi(token=bot_token)
    bot_api = bot_VK.get_api()

    user_VK = vk_api.VkApi(token=my_token)
    user_api = user_VK.get_api()

    time = my_group_time(user_api, group_id)
    post = new_texts_post(user_api, group_id, 'test',
                          date=unix_time_convert(time))

