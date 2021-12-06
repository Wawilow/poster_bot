import unittest
from new_post import *


class test_new_post(unittest.TestCase):
    def test_time_to_post(self):
        self.assertEqual(time_to_post([6, 20], [[7, 30], [11, 50], [17, 0]]), [False, [7, 30]], 'should be ok')
        self.assertEqual(time_to_post([7, 30], [[7, 30], [11, 50], [17, 0]]), [False, [11, 50]], 'should be ok')
        self.assertEqual(time_to_post([8, 50], [[7, 30], [11, 50], [17, 0]]), [False, [11, 50]], 'should be ok')
        self.assertEqual(time_to_post([11, 50], [[7, 30], [11, 50], [17, 0]]), [False, [17, 0]], 'should be ok')
        self.assertEqual(time_to_post([14, 50], [[7, 30], [11, 50], [17, 0]]), [False, [17, 0]], 'should be ok')
        self.assertEqual(time_to_post([17, 0], [[7, 30], [11, 50], [17, 0]]), [True, [7, 30]], 'should be ok')


if __name__ == '__main__':
    # vk api need time to sleep, and need run each test simple
    unittest.main()