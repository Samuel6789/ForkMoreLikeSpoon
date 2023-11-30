from __future__ import annotations
import unittest
from typing import List
from azul.interfaces import UsedTilesGiveInterface
from azul.simple_types import Tile, STARTING_PLAYER, RED, GREEN, Points
from azul.floor import Floor


class FakeUsedTiles(UsedTilesGiveInterface):
    tiles_given: List[Tile]

    def __init__(self) -> None:
        self.tiles_given = []

    def give(self, tiles: List[Tile]) -> None:
        self.tiles_given.extend(tiles)


class TestFloor(unittest.TestCase):
    def setUp(self) -> None:
        self.used_tiles: FakeUsedTiles = FakeUsedTiles()
        self.floor: Floor = Floor(
            [Points(1), Points(2), Points(2)], self.used_tiles)

    def test_tiles(self) -> None:
        tiles = [STARTING_PLAYER, RED, GREEN, RED]
        self.assertCountEqual(self.floor.state(), "")
        self.floor.put(tiles)
        self.assertCountEqual(self.floor.state(), "SRRG")
        points: Points = self.floor.finish_round()
        self.assertEqual(str(points), "7")
        self.assertCountEqual(tiles, self.used_tiles.tiles_given)
        self.assertCountEqual(self.floor.state(), "")
        tiles2: List[Tile] = [RED, GREEN]
        self.floor.put(tiles2[0:1])
        self.assertCountEqual(self.floor.state(), "R")
        self.floor.put(tiles2[1:2])
        self.assertCountEqual(self.floor.state(), "RG")
        self.floor.put([])
        self.assertCountEqual(self.floor.state(), "RG")
        points2: Points = self.floor.finish_round()
        self.assertEqual(str(points2), "3")
        self.assertCountEqual(tiles+tiles2, self.used_tiles.tiles_given)
        self.assertCountEqual(self.floor.state(), "")


if __name__ == '__main__':
    unittest.main()
