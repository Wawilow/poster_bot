import vk_api
from datetime import datetime
from time_convert import datatime_convert

def last_post(VK, groupId):
    params = {"owner_id": f'-{groupId}', "count": f'1'}
    time_post = int(f"{VK.wall.get(**params)['items'][0]['date']}")
    time_post = datetime.utcfromtimestamp(time_post).strftime('%Y-%m-%d %H:%M:%S')
    time_post = [*time_post.split(' ')[0].split('-'), *time_post.split(' ')[1].split(':')]
    time_post = datatime_convert(time_post, delta_hours=3)
    return time_post


def last_postponed_post(VK, groupId):
    params = {"owner_id": f'-{groupId}', "count": f'1', "filter": f'postponed'}
    time_post = int(f"{VK.wall.get(**params)['items'][0]['date']}")
    time_post = datetime.utcfromtimestamp(time_post).strftime('%Y-%m-%d %H:%M:%S')
    time_post = [*time_post.split(' ')[0].split('-'), *time_post.split(' ')[1].split(':')]
    time_post = datatime_convert(time_post, delta_hours=3)
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