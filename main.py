from last_post import last_post, last_postponed_post
import vk_api


def print_hi(name):
    print(f'Hi, {name}')


if __name__ == '__main__':
    token = 'cb0400ae1b14d0875b4803640297401794c9d0984e0585a5521672c3f9aa60e88c856f5ce2248b640ef60'  # тестовое сообщество https://vk.com/algoritms_bot
    main_token = 'ad135a8d6e65aa945e86f32aa44e9fd8f5ce4977a18a8b85a12ac9b3079c991c46699611ff17e7679bff6'  # личный токен моего аккаунта,
    # можешь сделать свой, для этого перейди по ссылке https://oauth.vk.com/authorize?client_id=7594388&scope=wall,offline&redirect_uri=http://api.vk.com/blank.html&response_type=token
    vk_api = vk_api.VkApi(token=main_token)
    VK = vk_api.get_api()
    groupId = '204098688'  # id тестового паблика

    print_hi('PyCharm')
    la = last_postponed_post(VK, groupId)
    print(f'postponed post {la}')
    la = last_post(VK, groupId)
    print(f'just post {la}')