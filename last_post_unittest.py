import unittest
from last_post import *


# data_time_convert
# all_post
# all_postponed_post_information
# last_post
# all_post
# last_postponed_post

class Testdata_time_convert(unittest.TestCase):
    def test_date_delta(self):
        # if send small date
        self.assertEqual(data_time_convert([2011, 11, 4]),
                         datetime.date(2011, 11, 4),
                         'should be ok')
        self.assertEqual(data_time_convert([2011, 11, 4], delta_days=3),
                         datetime.date(2011, 11, 7),
                         'should be ok')
        # if send big date
        self.assertEqual(data_time_convert([2011, 11, 4, 2, 3, 43]),
                         datetime.datetime(2011, 11, 4, 2, 3, 43, 0),
                         'should be ok')
        self.assertEqual(data_time_convert([2011, 11, 4, 2, 3, 43], delta_days=2),
                         datetime.datetime(2011, 11, 6, 2, 3, 43, 0),
                         'should be ok')
        self.assertEqual(data_time_convert([2011, 11, 4, 2, 3, 43], delta_hours=3),
                         datetime.datetime(2011, 11, 4, 5, 3, 43, 0),
                         'should be ok')
        self.assertEqual(data_time_convert([2011, 11, 4, 2, 3, 43], delta_minutes=4),
                         datetime.datetime(2011, 11, 4, 2, 7, 43, 0),
                         'should be ok')
        self.assertEqual(data_time_convert([2011, 11, 4, 2, 3, 43], delta_days=1, delta_hours=8),
                         datetime.datetime(2011, 11, 5, 10, 3, 43, 0),
                         'should be ok')
        self.assertEqual(data_time_convert([2011, 11, 4, 2, 3, 43], delta_hours=8, delta_minutes=5),
                         datetime.datetime(2011, 11, 4, 10, 8, 43, 0),
                         'should be ok')
        self.assertEqual(data_time_convert([2011, 11, 4, 2, 3, 43], delta_days=1, delta_minutes=15),
                         datetime.datetime(2011, 11, 5, 2, 18, 43, 0),
                         'should be ok')
        self.assertEqual(data_time_convert([2011, 11, 4, 2, 3, 43], delta_days=21, delta_hours=3, delta_minutes=17),
                         datetime.datetime(2011, 11, 25, 5, 20, 43, 0),
                         'should be ok')
    def test_all_postponed_post(self):
        my_token = '7590a1ae275d8b38b843371b2d9c4b64b196df60e43284e50e246f984c22b0f2c3cfe21a159f450d286a2'
        group_id = 204098688
        user_VK = vk_api.VkApi(token=my_token)
        user_api = user_VK.get_api()
        # edit variable to run test
        self.assertEqual(all_postponed_post(user_api, group_id, count=100),
                         user_api.wall.get(**{"owner_id": f'-{group_id}', "count": f'{100}', "filter": f'postponed'}),
                         'must be ok')
    def test_last_post(self):
        my_token = '7590a1ae275d8b38b843371b2d9c4b64b196df60e43284e50e246f984c22b0f2c3cfe21a159f450d286a2'
        group_id = 204098688
        user_VK = vk_api.VkApi(token=my_token)
        user_api = user_VK.get_api()
        # edit variable to run test
        self.assertEqual(last_post(user_api, group_id),
                         user_api.wall.get(**{"owner_id": f'-{group_id}', "count": f'1'}),
                         'must be ok')
    def test_last_post_date(self):
        my_token = '7590a1ae275d8b38b843371b2d9c4b64b196df60e43284e50e246f984c22b0f2c3cfe21a159f450d286a2'
        group_id = 204098688
        user_VK = vk_api.VkApi(token=my_token)
        user_api = user_VK.get_api()
        # edit variable to run test
        self.assertEqual(last_post_date(user_api, group_id, unix_time=True),
                         user_api.wall.get(**{"owner_id": f'-{group_id}', "count": f'1'})['items'][0]['date'],
                         'must be ok')
        self.assertEqual(last_post_date(user_api, group_id, unix_time=False),
                         datetime.datetime.utcfromtimestamp
                         (user_api.wall.get(**{"owner_id": f'-{group_id}', "count": f'1'})['items'][0]['date']),
                         'must be ok')
    def test_all_post(self):
        my_token = '7590a1ae275d8b38b843371b2d9c4b64b196df60e43284e50e246f984c22b0f2c3cfe21a159f450d286a2'
        group_id = 204098688
        user_VK = vk_api.VkApi(token=my_token)
        user_api = user_VK.get_api()
        # edit variable to run test
        self.assertEqual(all_post(user_api, group_id, postponed=False),
                         user_api.wall.get(**{"owner_id": f'-{group_id}', "count": f'{100}'}),
                         'must be ok')
        self.assertEqual(all_post(user_api, group_id, postponed=True),
                         user_api.wall.get(**{"owner_id": f'-{group_id}', "count": f'{100}', "filter": f'postponed'}),
                         'must be ok')


if __name__ == '__main__':
    # vk api need time to sleep, and need run each test simple
    unittest.main()
