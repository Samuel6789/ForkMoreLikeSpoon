from __future__ import annotations
import unittest
from typing import List
from azul.simple_types import Tile, STARTING_PLAYER, RED, GREEN, Points
from azul.tileSources import TileSource, tableCenter

class TestTileSources(unittest.TestCase):
    def setUp(self) -> None:
        self.tileSources: TileSource = TileSource()
        self.center: tableCenter = tableCenter()


    def test_tileSources(self) -> None:
        self.assertTrue(self.tileSources.isEmpty())
        self.assertEqual(self.tileSources.tiles, [])
        self.tileSources.tiles = [RED, RED, GREEN, RED, GREEN]
        self.assertEqual(self.tileSources.take(1), [RED, RED, RED])
        self.assertEqual(self.tileSources.state(), "GG")
        self.assertEqual(self.tileSources.take(4), [GREEN, GREEN])
        self.assertTrue(self.tileSources.state() == "")
        self.assertTrue(self.center.state() == "S")
        self.center.add([RED, RED, GREEN, RED, GREEN])
        self.assertTrue(self.center.state() == "SRRGRG")
        self.assertFalse(self.center.isEmpty())
        self.assertEqual(self.center.take(1), [STARTING_PLAYER, RED, RED, RED])
        self.assertEqual(self.center.state(), "GG")
        self.center.take(4)
        self.assertEqual(self.center.take(4), [])

if __name__ == '__main__':
    unittest.main()