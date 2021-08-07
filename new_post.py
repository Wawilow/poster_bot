import vk_api
from vk_api.upload import VkUpload
from time_convert import for_vk_post_convert
from time_convert import one_day_plus_time, time_now


def write_msg(user_id, message, api):
    if message == 'Готово':
        write_msg_with_photo(user_id, message)
    else:
        api.messages.send(user_id=user_id, message=str(message), random_id=randrange(999999999))


def write_msg_with_photo(VK, api, user_id, message, Photo):
    upload = vk_api.VkUpload(VK)
    photo = upload.photo_messages(str(Photo))
    owner_id = photo[0]['owner_id']
    photo_id = photo[0]['id']
    access_key = photo[0]['access_key']
    attachment = f'photo{owner_id}_{photo_id}_{access_key}'
    api.messages.send(user_id=user_id, message=str(message), random_id=randrange(999999999),
                      attachment=attachment)


def post_make(groupId='204098688', text='\n'):
    main_token = 'ad135a8d6e65aa945e86f32aa44e9fd8f5ce4977a18a8b85a12ac9b3079c991c46699611ff17e7679bff6'
    vk_api = VkApi(token=main_token)
    VK = vk_api.get_api()
    new_texts_post(VK, groupId,
                    '#АдекватныеМемы',
                    data=unixtime_convert(time_to_post(
                        time=[*str(last_postponed_post(VK, groupId)).split(' ')[0].split('-'),
                              *str(last_postponed_post(VK, groupId)).split(' ')[1].split(':')], fall=True))
                    )


def new_texts_post(VK, groupId, textPost, data=for_vk_post_convert()):
    attachments = []
    params = {"owner_id": f'-{groupId}', "message": textPost, "attachments": attachments, 'publish_date': data}
    VK.wall.post(**params)


def new_image_post(VK, groupId, time_to_post, img, text='', albomId=279018273):
    upload = VkUpload(VK)
    photo = upload.photo(str(img), albomId)
    owner_id = photo[0]['owner_id']
    photo_id = photo[0]['id']
    attachments = f'photo{owner_id}_{photo_id}'
    params = {"owner_id": f'-{groupId}', "message": text, "publish_date": time_to_post,
              "attachments": attachments}
    return VK.wall.post(**params)


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
    # token = '54041327cd1967dc10fcce01620b625c4e6949672e5b754f10f7e7920510aabb58f3babe8febf1df4c34f'
    # #токен основного аккаунта https://vk.com/neural_pushkin
    token = 'cb0400ae1b14d0875b4803640297401794c9d0984e0585a5521672c3f9aa60e88c856f5ce2248b640ef60'
    # тестовое сообщество https://vk.com/algoritms_bot
    main_token = '7590a1ae275d8b38b843371b2d9c4b64b196df60e43284e50e246f984c22b0f2c3cfe21a159f450d286a2'
    # личный токен моего аккаунта,
    # можешь сделать свой, для этого перейди по ссылке
    # https://oauth.vk.com/authorize?client_id=7594388&scope=wall,offline&redirect_uri=http://api.vk.com/blank.html&response_type=token
    vk_api = vk_api.VkApi(token=main_token)
    VK = vk_api.get_api()
    # groupId = '204098688'  # id тестового паблика
    # groupId = '204952505'  #id основного паблика
    groupId = 204098688
    albomId = 279018273
    print(new_image_post(VK, groupId,
                         for_vk_post_convert(),
                         img='image.png', albomId=albomId))