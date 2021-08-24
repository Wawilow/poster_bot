import unittest
from time_convert import *


class Testdata_last_post_unittest(unittest.TestCase):
    def test_date_delta(self):
        # if send small date
        self.assertEqual(time_now(),
                         [*str(datetime.datetime.now()).split(' ')[0].split('-'),
                          *(str(datetime.datetime.now()).split(' ')[1].split('.')[0]).split(':')],
                         'should be ok')


if __name__ == '__main__':
    # vk api need time to sleep, and need run each test simple
    unittest.main()