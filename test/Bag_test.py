from __future__ import annotations
import unittest
from Assignment.azul import Bag
from Assignment.azul.simple_types import *


class MyTestCase(unittest.TestCase):
    def test_take_10_multiple_times(self):
        bag = Bag.Bag()
        self.assertEqual(100, len(bag.tiles))
        expected_list = [BLACK, RED, RED, BLUE, BLUE, RED, GREEN, BLACK, YELLOW, YELLOW]
        self.assertEqual(expected_list, bag.take(10))
        self.assertEqual(90, len(bag.tiles))
        expected_list2 = [BLACK, RED, BLUE, BLUE, YELLOW, YELLOW, BLUE, BLACK, BLACK, YELLOW]
        self.assertEqual(expected_list2, bag.take(10))
        self.assertEqual(80, len(bag.tiles))

    def test_take_invalid_amounts(self):
        bag = Bag.Bag()
        self.assertEqual([], bag.take(0))
        self.assertEqual([], bag.take(-1))
        self.assertEqual([], bag.take(101))
        self.assertEqual(100, len(bag.tiles))


if __name__ == '__main__':
    unittest.main()
