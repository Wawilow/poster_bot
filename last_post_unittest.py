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
    def test_wrong_type(self):
        pass


if __name__ == '__main__':
    unittest.main()
