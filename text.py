import requests
import json
import vk
from new_post import new_image_post

from icecream import ic


token = '7590a1ae275d8b38b843371b2d9c4b64b196df60e43284e50e246f984c22b0f2c3cfe21a159f450d286a2' # здесь токен
group_id = 204098688 # здесь id группы


def getWallUploadServer(api_vk):
    upload_url = api_vk.photos.getWallUploadServer(group_id=group_id, v=5.131)
    return upload_url['upload_url']


def save_r(api_vk, flag=False):
    save_result = (api_vk.photos.saveWallPhoto(group_id=group_id, photo=upload_response['photo'], server=upload_response['server'], hash=upload_response['hash'], v=5.131))[0]
    if flag:
        return save_result
    return f"""photo{save_result['owner_id']}_{save_result['id']}&access_key={save_result['access_key']}"""


def main():
    global upload_response

    api_vk = vk.API(vk.Session(access_token=token))

    upload_url = getWallUploadServer(api_vk)

    file = {'file1': open('image.png', 'rb')}

    upload_response = requests.post(upload_url, files=file).json()
    print(upload_response)
    save_result = save_r(api_vk, flag=True)
    print(save_result)

    print(f'save result - "{save_result}"')
    # result2 = api_vk.wall.post(attachments=save_result, owner_id=-group_id, access_token=token, from_group=1, v=1.131)
    # print(result2)


if __name__ == '__main__':
    # a = [{'album_id': -14, 'date': 1632331515, 'id': 457246887, 'owner_id': 503409544, 'has_tags': False, 'access_key': 'd80be1e9bcdd6ea5bc', 'sizes': [{'height': 75, 'url': 'https://sun9-8.userapi.com/impg/m2ZOVYfSIn2ghH4R7mzZQE1t9Naj-BWJ7jBdIg/-aQvl1r2dpI.jpg?size=71x75&quality=96&sign=b29a8a1fe1ccf9d3e3386f1c5e388299&c_uniq_tag=kugxecW5PnNZnWZFzHHPtAUGD1uN7o3UouMWq6GbeVs&type=album', 'type': 's', 'width': 72}, {'height': 130, 'url': 'https://sun9-8.userapi.com/impg/m2ZOVYfSIn2ghH4R7mzZQE1t9Naj-BWJ7jBdIg/-aQvl1r2dpI.jpg?size=124x130&quality=96&sign=623e2b49d0b57013be913a3a767b9d1d&c_uniq_tag=hAoFvLeKBAsNNzG7N4FrUpgE6E08SFzsPsExM9VI5UE&type=album', 'type': 'm', 'width': 124}, {'height': 536, 'url': 'https://sun9-8.userapi.com/impg/m2ZOVYfSIn2ghH4R7mzZQE1t9Naj-BWJ7jBdIg/-aQvl1r2dpI.jpg?size=510x536&quality=96&sign=ec08ba7a2f2eafce40069efbc27ed1ba&c_uniq_tag=P_FX5Wctie-KqP6jiZT_lsSUfT9y4g9dXeVTChrt9z4&type=album', 'type': 'x', 'width': 510}, {'height': 137, 'url': 'https://sun9-8.userapi.com/impg/m2ZOVYfSIn2ghH4R7mzZQE1t9Naj-BWJ7jBdIg/-aQvl1r2dpI.jpg?size=130x137&quality=96&sign=42f0586c0418a6d8b3ca306354b86ac7&c_uniq_tag=SvER9MbjGrFEjTaGIAmswLTe06IUiFct2bXM8_2hbjs&type=album', 'type': 'o', 'width': 130}, {'height': 210, 'url': 'https://sun9-8.userapi.com/impg/m2ZOVYfSIn2ghH4R7mzZQE1t9Naj-BWJ7jBdIg/-aQvl1r2dpI.jpg?size=200x210&quality=96&sign=12076e2dea20ed763f77381413f010ab&c_uniq_tag=ynKF-qctk5Gktmn-Lt-OcZF71J9SMQjhBbb4FtS5FRE&type=album', 'type': 'p', 'width': 200}, {'height': 336, 'url': 'https://sun9-8.userapi.com/impg/m2ZOVYfSIn2ghH4R7mzZQE1t9Naj-BWJ7jBdIg/-aQvl1r2dpI.jpg?size=320x336&quality=96&sign=bbce675901d0e71895e9a9fddcff9e08&c_uniq_tag=8Ek9jqQQU-InsDcLQXE45LANOXQ2MI_aVRRKaPihcnE&type=album', 'type': 'q', 'width': 320}, {'height': 536, 'url': 'https://sun9-8.userapi.com/impg/m2ZOVYfSIn2ghH4R7mzZQE1t9Naj-BWJ7jBdIg/-aQvl1r2dpI.jpg?size=510x536&quality=96&sign=ec08ba7a2f2eafce40069efbc27ed1ba&c_uniq_tag=P_FX5Wctie-KqP6jiZT_lsSUfT9y4g9dXeVTChrt9z4&type=album', 'type': 'r', 'width': 510}], 'text': ''}]
    main()
