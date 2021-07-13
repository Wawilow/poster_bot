from last_post import last_postponed_post
from vk_api import VkApi
from new_post import time_to_post, new_texts_post
from time_convert import unixtime_convert

from icecream import ic

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


if __name__ == '__main__':
    post_make(groupId='198242788')

