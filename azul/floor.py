from __future__ import annotations
from typing import List
from itertools import chain, repeat, islice
from interfaces import UsedTilesGiveInterface
from simple_types import Tile, compress_tile_list, Points


class Floor:
    _point_pattern: List[Points]
    _used_tiles: UsedTilesGiveInterface
    _tiles: List[Tile]

    def __init__(self, point_pattern: List[Points], used_tiles: UsedTilesGiveInterface):
        self._point_pattern = point_pattern.copy()
        self._used_tiles = used_tiles
        self._tiles = []

    def put(self, tiles: List[Tile]) -> None:
        self._tiles.extend(tiles)

    def finish_round(self) -> Points:
        extended_pattern = chain(
            self._point_pattern, repeat(self._point_pattern[-1]))
        points: Points = Points.sum(
            list(islice(extended_pattern, 0, len(self._tiles))))
        self._used_tiles.give(self._tiles.copy())
        self._tiles = []
        return points

    def state(self) -> str:
        return compress_tile_list(self._tiles)
