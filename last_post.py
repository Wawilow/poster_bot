import vk_api
from datetime import datetime


def data_time_convert(data, delta=0, delta_hours=0):
    # в дату можно 1)дататам ноу 2)год, месяц, дата
    # 3)год, месяц, дата, час, минута, секунда
    # в дельту можно целое число, количество дней сколько при поюсовать
    try:
        delta = datetime.timedelta(days=delta, hours=delta_hours)
    except:
        return ('error delta convert')
    try:
        return data + delta
    except:
        if type(data) == type([]):
            try:
                if len(data) == 3:
                    data = datetime.date(data[0], data[1], data[2])
                    return data + delta
                elif len(data) == 6:
                    # data = datetime.date(data[0], data[1], data[2], data[3], data[4])
                    data = [int(i) for i in data]
                    data = datetime.datetime(data[0], data[1], data[2], data[3], data[4], data[5], 0)
                    # datetime.datetime(2011, 11, 4, 0, 5, 23, 283000)
                    # >> > datetime.fromisoformat('2011-11-04 00:05:23.283+00:00')
                    return data + delta
            except:
                return ('error list ==> date convert')
        return ('error summ data')


def all_postponed_post(VK, groupId):
    params = {"owner_id": f'-{groupId}', "count": f'100', "filter": f'postponed'}
    time_post = VK.wall.get(**params)
    # ic(time_post)
    return time_post['items']


def last_post(VK, groupId):
    params = {"owner_id": f'-{groupId}', "count": f'100'}
    time_post = int(f"{VK.wall.get(**params)['items'][-1]['date']}")
    time_post = datetime.utcfromtimestamp(time_post).strftime('%Y-%m-%d %H:%M:%S')
    time_post = [*time_post.split(' ')[0].split('-'), *time_post.split(' ')[1].split(':')]
    time_post = data_time_convert(time_post, delta_hours=3)
    return time_post


def last_postponed_post(VK, groupId):
    params = {"owner_id": f'-{groupId}', "count": f'100', "filter": f'postponed'}
    try:
        time_post = int(f"{VK.wall.get(**params)['items'][-1]['date']}")
        time_post = datetime.utcfromtimestamp(time_post).strftime('%Y-%m-%d %H:%M:%S')
        time_post = [*time_post.split(' ')[0].split('-'), *time_post.split(' ')[1].split(':')]
        time_post = data_time_convert(time_post, delta_hours=3)
    except:
        return [False, 'no postponed post']
    return time_post


if __name__ == '__main__':
    main_token = 'ad135a8d6e65aa945e86f32aa44e9fd8f5ce4977a18a8b85a12ac9b3079c991c46699611ff17e7679bff6'  # личный токен моего аккаунта,
    # можешь сделать свой, для этого перейди по ссылке
    # https://oauth.vk.com/authorize?client_id=7594388&scope=wall,offline&redirect_uri=http://api.vk.com/blank.html&response_type=token
    vk_api = vk_api.VkApi(token=main_token)
    VK = vk_api.get_api()
    groupId = '204098688'  # id тестового паблика
    # groupId = '204952505'  #id основного паблика

    # print(last_post(VK, groupId))
    print(last_postponed_post(VK, groupId))