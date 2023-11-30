from __future__ import annotations
import unittest
from typing import List
from azul.simple_types import Tile, STARTING_PLAYER, RED, GREEN, Points
from azul.bag import Bag
from azul.tableArea import TableArea
from azul.factory import Factory
from azul.usedTiles import usedTiles

class testTableArea(unittest.TestCase):
    def setUp(self) -> None:
        self.bag: Bag = Bag(usedTiles())
        self.table: TableArea = TableArea(2, self.bag)

    def test_TableArea(self) -> None:
        self.assertTrue(len(self.table.factories) == 5)
        self.assertEqual(self.table.state(), "Factories:      | Center: S")
        self.table.startNewRound()
        self.assertFalse(self.table.isRoundEnd())
        self.table.factories[0].tiles = [RED, RED, GREEN, GREEN]
        self.assertEqual(self.table.take(0, 1), [RED, RED])
        for i in range(5):
            self.table.factories[i].tiles = []
        self.table.tableCenter.tiles = []
        self.assertTrue(self.table.isRoundEnd())

if __name__ == '__main__':
    unittest.main()