from __future__ import annotations
import unittest
from typing import List
from azul.simple_types import Tile, STARTING_PLAYER, RED, GREEN, Points
from azul.usedTiles import usedTiles
from azul.interfaces import bagState

class TestUsedTiles(unittest.TestCase):
    def setUp(self) -> None:
        self.used: usedTiles = usedTiles()
        self.bag: bagState = bagState()


    def test_usedTiles(self) -> None:
        self.used.give([RED, GREEN])
        self.assertTrue(self.used.state() == "RG")
        self.bag.fakeAdd(self.used.takeAll())
        self.assertTrue(self.used.state() == "")
        self.used.give([STARTING_PLAYER])
        self.assertTrue(self.used.state() == "")
        self.assertEqual(self.used.takeAll(), [])


if __name__ == '__main__':
    unittest.main()