import unittest
from time_convert import *


class test_time_convert(unittest.TestCase):
    def test_time_now(self):
        self.assertEqual(time_now(),
                         [*str(datetime.datetime.now()).split(' ')[0].split('-'),
                          *(str(datetime.datetime.now()).split(' ')[1].split('.')[0]).split(':')],
                         'should be ok')


    def test_unix_time_convert(self):
        self.assertEqual(unix_time_convert(datetime.datetime(2011, 2, 15, 4, 45, 13)), 1297734313.0, 'should be ok')
        self.assertEqual(unix_time_convert(datetime.date(2011, 2, 15)), 1297717200.0, 'should be ok')


    def test_data_time_list_convert(self):
        self.assertEqual(
            data_time_list_convert(datetime.datetime(2101, 11, 23, 10, 17, 23)), [2101, 11, 23, 10, 17, 23],
            'should be ok')
        self.assertEqual(
            data_time_list_convert(datetime.date(2101, 11, 23)), [2101, 11, 23, 0, 0, 0],
            'should be ok')


if __name__ == '__main__':
    # vk api need time to sleep, and need run each test simple
    unittest.main()