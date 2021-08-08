import vk_api
import datetime


def data_time_convert(data, delta=0, delta_hours=0):
    # в дату можно 1)дататам ноу 2)год, месяц, дата
    # 3)год, месяц, дата, час, минута, секунда
    # в дельту можно целое число, количество дней сколько при поюсовать
    try:
        if delta != 0:
            if delta_hours != 0:
                delta = datetime.timedelta(days=delta, hours=delta_hours)
            else:
                delta = datetime.timedelta(days=delta)
        else:
            if delta_hours != 0:
                delta = datetime.timedelta(hours=delta_hours)
            else:
                delta = None
    except:
        return ('error delta convert')
    try:
        if delta != None:
            return data + delta
        else:
            return data
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
        print(data, delta)
        return ('error summ data')


def all_postponed_post(VK, groupId):
    params = {"owner_id": f'-{groupId}', "count": f'100', "filter": f'postponed'}
    time_post = VK.wall.get(**params)
    # ic(time_post)
    return time_post['items']


def all_postponed_post_information(VK, groupId, id):
    posts = all_postponed_post(VK, groupId)
    post = 'Такого поста не существует'
    for i in posts:
        if i['id'] == id:
            post = i
    return post


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
    try:
        time_post = int(f"{VK.wall.get(**params)['items'][-1]['date']}")
        time_post = datetime.datetime.utcfromtimestamp(time_post).strftime('%Y-%m-%d %H:%M:%S')
        time_post = [*time_post.split(' ')[0].split('-'), *time_post.split(' ')[1].split(':')]
        time_post = data_time_convert(time_post, delta_hours=3)
    except:
        return data_time_convert(datetime.datetime.now(), delta_hours=1)
    return time_post


if __name__ == '__main__':
    main_token = '7590a1ae275d8b38b843371b2d9c4b64b196df60e43284e50e246f984c22b0f2c3cfe21a159f450d286a2'  # личный токен моего аккаунта,
    # можешь сделать свой, для этого перейди по ссылке
    # https://oauth.vk.com/authorize?client_id=7594388&scope=wall,offline&redirect_uri=http://api.vk.com/blank.html&response_type=token
    vk_api = vk_api.VkApi(token=main_token)
    VK = vk_api.get_api()
    groupId = '204098688'  # id тестового паблика
    # groupId = '204952505'  #id основного паблика

    # print(last_post(VK, groupId))
    print(all_postponed_post(VK, groupId)[0])
    VK.w