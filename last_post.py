import vk_api
import datetime


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
        params = {"owner_id": f'-{group_id}', "count": f'1'}
        # make request to vk api
        time_post = user_api.wall.get(**params)['items'][0]['date']
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


def all_post(user_api, group_id, count=100, postponed=False):
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


def last_postponed_post(user_api, group_id):
    # check type all variable, if something wrong return error
    if str(type(user_api)) != "<class 'vk_api.vk_api.VkApiMethod'>":
        return 'user_api type error'
    if type(group_id) != type(1):
        return 'group_id type error'
    # make request to vk api
    try:
        params = {"owner_id": f'-{group_id}', "count": f'1', "filter": f'postponed'}
        time_post = user_api.wall.get(**params)
        return time_post
    except:
        return 'get wall error'


if __name__ == '__main__':
    pass
