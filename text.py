import vk_api
import time
import json
import ast

from icecream import ic
print = ic


atchs2 = {'message': {'date': 1626476325, 'from_id': 503409544, 'id': 238, 'out': 0, 'peer_id': 503409544, 'text': '', 'conversation_message_id': 196, 'fwd_messages': [], 'important': False, 'random_id': 0, 'attachments': [{'type': 'photo', 'photo': {'album_id': -3, 'date': 1626476325, 'id': 457245532, 'owner_id': 503409544, 'has_tags': False, 'access_key': '9126034b0168b0211f', 'sizes': [{'height': 48, 'url': 'https://sun9-45.userapi.com/impg/fSGbS5KsM7uwY-Mt8qrb_a7FelrHdkGC83LXYA/OlzhSWixpGQ.jpg?size=75x48&quality=96&sign=bf41d0a3bfa7d95ed1e041a25b0bf954&c_uniq_tag=PYbHUlyEJEbzQTqgKT755AtxXJrjT2qnDK85AWNOaGw&type=album', 'type': 's', 'width': 75}, {'height': 83, 'url': 'https://sun9-45.userapi.com/impg/fSGbS5KsM7uwY-Mt8qrb_a7FelrHdkGC83LXYA/OlzhSWixpGQ.jpg?size=130x83&quality=96&sign=74f58c17f88e3ed6501902712d031d45&c_uniq_tag=SFYqBxdglcg2aw9_IMahHzmatEeymh_Tul4gpNW8wa8&type=album', 'type': 'm', 'width': 130}, {'height': 372, 'url': 'https://sun9-45.userapi.com/impg/fSGbS5KsM7uwY-Mt8qrb_a7FelrHdkGC83LXYA/OlzhSWixpGQ.jpg?size=585x372&quality=96&sign=7a4133443601a5a0e98b5f2b2109ebf4&c_uniq_tag=SikHCMv0GP9Kb2ZhaW3TDy7RVaKDJFRviu_ofBAKVsg&type=album', 'type': 'x', 'width': 585}, {'height': 87, 'url': 'https://sun9-45.userapi.com/impg/fSGbS5KsM7uwY-Mt8qrb_a7FelrHdkGC83LXYA/OlzhSWixpGQ.jpg?size=130x87&quality=96&crop=14,0,556,372&sign=239234c68650d72d1335d960201ec3d2&c_uniq_tag=LeFGnL5MB_lUv4cP-edwEOyvNa2SDmVFGLwr4X6ol20&type=album', 'type': 'o', 'width': 130}, {'height': 133, 'url': 'https://sun9-45.userapi.com/impg/fSGbS5KsM7uwY-Mt8qrb_a7FelrHdkGC83LXYA/OlzhSWixpGQ.jpg?size=200x133&quality=96&crop=13,0,559,372&sign=e797e86cba084599fe0a1e0009a12864&c_uniq_tag=asetnJlIQYF31lruI3OW-3x1mqzX-AWD_5oi3XgY25g&type=album', 'type': 'p', 'width': 200}, {'height': 213, 'url': 'https://sun9-45.userapi.com/impg/fSGbS5KsM7uwY-Mt8qrb_a7FelrHdkGC83LXYA/OlzhSWixpGQ.jpg?size=320x213&quality=96&crop=13,0,559,372&sign=f2ca9c53a3bdcba74a7da0a5567214a0&c_uniq_tag=XckN9fRO15Qo4DHSusy7CmnQm26MqdCgWcc1rzmedsY&type=album', 'type': 'q', 'width': 320}, {'height': 340, 'url': 'https://sun9-45.userapi.com/impg/fSGbS5KsM7uwY-Mt8qrb_a7FelrHdkGC83LXYA/OlzhSWixpGQ.jpg?size=510x340&quality=96&crop=13,0,558,372&sign=86fed9c3275062dcde4b25d91775b3e0&c_uniq_tag=YeBoa4vdMZq8f_K9In_R6oQut7elFfdizLipLXXszkA&type=album', 'type': 'r', 'width': 510}], 'text': ''}}], 'is_hidden': False}, 'client_info': {'button_actions': ['text', 'vkpay', 'open_app', 'location', 'open_link', 'callback', 'intent_subscribe', 'intent_unsubscribe'], 'keyboard': True, 'inline_keyboard': True, 'carousel': True, 'lang_id': 0}}
atchs = '{"Nikhil" : 1, "Akshat" : 2, "Akash" : 3}'
atchs2 = str(atchs2)
print(type(atchs))
atch = json.loads(atchs)
print(atch)
print(type(atch))
atch2 = ast.literal_eval(atchs2)
print(atch2)