import random
from unittest import TestCase

from numpy import sort

from algorytmy import buble_sort


class Test(TestCase):
    message = 'Looks like something is not ok.'

    def test_buble_sort_list(self):
        list_1 = [1, 2, 3, 4]
        list_2 = buble_sort([3, 4, 2, 1])
        self.assertEqual(list_1, list_2, msg=self.message)

    def test_buble_sort_random(self):
        list_1 = random.sample(range(10, 30), 5)
        list_2 = buble_sort(list_1)
        self.assertEqual(list_1, list_2, msg=self.message)

    def test_equal(self):
        list_1 = [1, 2, 3, 4]
        list_2 = buble_sort([3, 4, 2, 1])
        self.assertEqual(list_1, list_2, )
