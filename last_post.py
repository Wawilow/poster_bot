import vk_api
import datetime
import time

from icecream import ic

# convert time
def data_time_convert(data, delta_days=0, delta_hours=0, delta_minutes=0):
    # variable can be
    # 1) data time type
    # 2) list type [year, month, date]
    # 3) big list [year, month, date, hour, minute, second]
    # delta must be type int

    # here i check all variable type
    if type(data) not in [type(datetime.datetime.now()), type(datetime.date(2011, 11, 4)), type([])]:
        return f'data type error'
    if type(delta_days) != type(1):
        return f'delta_days type error'
    if type(delta_hours) != type(1):
        return f'delta_hours type error'
    if type(delta_minutes) != type(1):
        return f'delta_minutes type error'
    try:
        # try delta in datetime delta convert
        delta = datetime.timedelta(days=delta_days, hours=delta_hours, minutes=delta_minutes)
    except:
        return 'error delta convert'
    if type(data) == type([]):
        try:
            if len(data) == 3:
                data = datetime.date(data[0], data[1], data[2])
                return data + delta
            elif len(data) == 6:
                data = [int(i) for i in data]
                data = datetime.datetime(data[0], data[1], data[2], data[3], data[4], data[5], 0)
                # datetime.datetime(2011, 11, 4, 0, 5, 23, 283000)
                # >> > datetime.from iso format('2011-11-04 00:05:23.283+00:00')
                return data + delta
        except:
            return 'error list ==> date convert'
    if type(data) == type(datetime.datetime(2011, 11, 4, 0, 0, 0, 0)) or type(data) == type(datetime.date(2011, 11, 4)):
        try:
            return data + delta
        except:
            return 'error sum data and delta'
    return 'error sum data'


# return all posts
def all_posts(user_api, group_id, count=100, postponed=False):
    # check type all variable, if something wrong return error
    if str(type(user_api)) != "<class 'vk_api.vk_api.VkApiMethod'>":
        return 'user_api type error'
    if type(group_id) != type(1):
        return 'group_id type error'
    if type(count) != type(1):
        return 'count type error'
    if type(postponed) != type(False):
        return 'postponed type error'
    # if you want get postponed post
    if postponed:
        postponed_params = {"owner_id": f'-{group_id}', "count": f'{count}', "filter": f'postponed'}
        try:
            postponed_post = user_api.wall.get(**postponed_params)
            return postponed_post
        except:
            return 'postponed wall get error'
    # if you dont want get postponed post
    else:
        params = {"owner_id": f'-{group_id}', "count": f'{count}'}
        try:
            post = user_api.wall.get(**params)
            return post
        except:
            return 'wall get error'


# return all published post
def all_post(user_api, group_id, count=100):
    # check type all variable, if something wrong return error
    if str(type(user_api)) != "<class 'vk_api.vk_api.VkApiMethod'>":
        return 'user_api type error'
    if type(group_id) != type(1):
        return 'group_id type error'
    if type(count) != type(1):
        return 'count type error'
    # make request to vk api
    try:
        params = {"owner_id": f'-{group_id}', "count": f'{count}'}
        time_post = user_api.wall.get(**params)
        return time_post
    except:
        return 'get wall error'


# return last published post
def last_post(user_api, group_id):
    # check type all variables
    if str(type(user_api)) != "<class 'vk_api.vk_api.VkApiMethod'>":
        return 'user_api type error'
    if type(group_id) != type(1):
        return 'group_id type error'
    # maybe here need check its bot api or user api, but it dosent meter and very hard to do
    try:
        # configure request
        params = {"owner_id": f'-{group_id}', "count": f'1'}
        # make request to vk api
        time_post = user_api.wall.get(**params)
    except:
        return 'wall ger error'
    return time_post


# return date last published post
def last_post_date(user_api, group_id, unix_time=True):
    # check type all variables
    if str(type(user_api)) != "<class 'vk_api.vk_api.VkApiMethod'>":
        return 'user_api type error'
    if type(group_id) != type(1):
        return 'group_id type error'
    if type(unix_time) != type(False):
        return 'unix_time type error'
    # maybe here need check its bot api or user api, but it dosent meter and very hard to do
    try:
        # configured request
        params = {"owner_id": f'-{group_id}', "count": f'100'}
        # make request to vk api
        time_post = user_api.wall.get(**params)['items'][-1]['date']
    except:
        return 'wall ger error'
    if unix_time:
        return time_post
    else:
        try:
            # if need not unixtime type make datatime type
            time_post = datetime.datetime.utcfromtimestamp(time_post)
            return time_post
        except:
            return 'convert time error'


# return all postponed post
def all_postponed_post(user_api, group_id, count=100):
    # check type all variable, if something wrong return error
    if str(type(user_api)) != "<class 'vk_api.vk_api.VkApiMethod'>":
        return 'user_api type error'
    if type(group_id) != type(1):
        return 'group_id type error'
    if type(count) != type(1):
        return 'count type error'
    # make request to vk api
    try:
        params = {"owner_id": f'-{group_id}', "count": f'{count}', "filter": f'postponed'}
        time_post = user_api.wall.get(**params)
        return time_post
    except:
        return 'get wall error'


# return last postponed post
def last_postponed_post(user_api, group_id):
    # check type all variable, if something wrong return error
    if str(type(user_api)) != "<class 'vk_api.vk_api.VkApiMethod'>":
        return 'user_api type error'
    if type(group_id) != type(1):
        return 'group_id type error'
    # make request to vk api
    try:
        params = {"owner_id": f'-{group_id}', "count": f'100', "filter": f'postponed'}
        time_post = user_api.wall.get(**params)
        if time_post['count'] == 0:
            return datetime.datetime.now()
        return time_post['items'][-1]
    except:
        return 'get wall error'


# return date last postponed post
def last_postponed_post_date(user_api, group_id, unix_time=False):
    # check type all variable, if something wrong return error
    if str(type(user_api)) != "<class 'vk_api.vk_api.VkApiMethod'>":
        return 'user_api type error'
    if type(group_id) != type(1):
        return 'group_id type error'
    # make request to vk api
    try:
        params = {"owner_id": f'-{group_id}', "count": f'100', "filter": f'postponed'}
        time_post = user_api.wall.get(**params)
        if time_post['count'] == 0:
            time_post = datetime.datetime.now()
            if not unix_time:
                return time_post
            else:
                return time.mktime(time_post.timetuple())
    except:
        return 'wall ger error'
    try:
        time_post = time_post['items'][-1]['date']
    except:
        return 'no postponed post'
    if unix_time:
        return time_post
    else:
        try:
            # if need not unixtime type make datatime type
            time_post = datetime.datetime.utcfromtimestamp(time_post)
            return time_post
        except:
            return 'convert time error'


if __name__ == '__main__':
    user_token = '76e9445d2039e9afde8fc845c4a1b02a155350bdd903a56b21d013bb6c99b5215b7e111c6a68fa0f5d84e'
    #user_token = '7590a1ae275d8b38b843371b2d9c4b64b196df60e43284e50e246f984c22b0f2c3cfe21a159f450d286a2'
    bot_token = 'cb0400ae1b14d0875b4803640297401794c9d0984e0585a5521672c3f9aa60e88c856f5ce2248b640ef60'

    bot_group_id = 204098688
    group_id = 198242788
    album_id = 279018273

    bot_VK = vk_api.VkApi(token=bot_token)
    bot_api = bot_VK.get_api()

    user_VK = vk_api.VkApi(token=user_token)
    user_api = user_VK.get_api()

    print(all_post(user_api, group_id))

    # last_p = data_time_convert(last_postponed_post_date(user_api, group_id), delta_hours=3)