import vk_api
import datetime


from icecream import ic


def data_time_convert(data, delta_days=0, delta_hours=0, delta_minutes=0):
    # variable can be
    # 1) datatime type
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
    if str(type(user_api)) != "<class 'vk_api.vk_api.VkApiMethod'>":
        return 'user_api type error'
    if type(group_id) != type(1):
        return 'group_id type error'
    if type(count) != type(1):
        return 'count type error'
    try:
        params = {"owner_id": f'-{group_id}', "count": f'{count}', "filter": f'postponed'}
        time_post = user_api.wall.get(**params)
        return time_post
    except:
        return 'get wall error'


def last_post(VK, groupId):
    params = {"owner_id": f'-{groupId}', "count": f'100'}
    time_post = int(f"{VK.wall.get(**params)['items'][-1]['date']}")
    time_post = datetime.datetime.utcfromtimestamp(time_post).strftime('%Y-%m-%d %H:%M:%S')
    time_post = [*time_post.split(' ')[0].split('-'), *time_post.split(' ')[1].split(':')]
    time_post = data_time_convert(time_post, delta_hours=3)
    return time_post


def all_post(VK, groupId, how_many=100):
    params = {"owner_id": f'-{groupId}', "count": f'{how_many}'}
    return VK.wall.get(**params)


def last_postponed_post(VK, groupId):
    params = {"owner_id": f'-{groupId}', "count": f'100', "filter": f'postponed'}
    if True:
        print(f"time post {params}")
        time_post = int(f"{VK.wall.get(**params)['items'][-1]['date']}")
        time_post = datetime.datetime.utcfromtimestamp(time_post).strftime('%Y-%m-%d %H:%M:%S')
        time_post = [*time_post.split(' ')[0].split('-'), *time_post.split(' ')[1].split(':')]
        time_post = data_time_convert(time_post, delta_hours=3)
    else:
        return data_time_convert(datetime.datetime.now(), delta_hours=1)
    return time_post


if __name__ == '__main__':
    main_token = '7590a1ae275d8b38b843371b2d9c4b64b196df60e43284e50e246f984c22b0f2c3cfe21a159f450d286a2'  # личный токен моего аккаунта,
    # можешь сделать свой, для этого перейди по ссылке
    # https://oauth.vk.com/authorize?client_id=7594388&scope=wall,offline&redirect_uri=http://api.vk.com/blank.html&response_type=token
    vk_api = vk_api.VkApi(token=main_token)
    VK = vk_api.get_api()
    groupId = '204098688'  # id тестового паблика
    ic(all_postponed_post(VK, groupId))
