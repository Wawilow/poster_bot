import vk_api
import datetime
from time_convert import for_vk_post_convert
from time_convert import one_day_plus_time, time_now


def new_texts_post(VK, groupId, textPost, data=for_vk_post_convert()):
    attachments = []
    params = {"owner_id": f'-{groupId}', "message": textPost, "attachments": attachments, 'publish_date': data}
    VK.wall.post(**params)


def new_image_post(img, text=''):
    attachments = []
    params = {"owner_id": f'-{groupId}', "message": textPost, "publish_date": for_vk_post_convert()
        , "attachments": attachments}
    VK.wall.post(**params)


def time_to_post(time, small=False, fall=False):
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
    textPost = 'тест'
    # textPost = input()
    # token = '54041327cd1967dc10fcce01620b625c4e6949672e5b754f10f7e7920510aabb58f3babe8febf1df4c34f'#токен основного аккаунта https://vk.com/neural_pushkin
    token = 'cb0400ae1b14d0875b4803640297401794c9d0984e0585a5521672c3f9aa60e88c856f5ce2248b640ef60'  # тестовое сообщество https://vk.com/algoritms_bot
    main_token = 'ad135a8d6e65aa945e86f32aa44e9fd8f5ce4977a18a8b85a12ac9b3079c991c46699611ff17e7679bff6'  # личный токен моего аккаунта,
    # можешь сделать свой, для этого перейди по ссылке https://oauth.vk.com/authorize?client_id=7594388&scope=wall,offline&redirect_uri=http://api.vk.com/blank.html&response_type=token
    vk_api = vk_api.VkApi(token=main_token)
    VK = vk_api.get_api()
    groupId = '204098688'  # id тестового паблика
    # groupId = '204952505'  #id основного паблика
    print(time_to_post([2021, 7, 19, 22, 27, 00]))