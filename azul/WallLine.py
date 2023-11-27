from __future__ import annotations
from typing import List, Optional
from interfaces import UsedTilesGiveInterface
from simple_types import Tile, compress_tile_list, Points, RED, BLUE, YELLOW, GREEN, BLACK, STARTING_PLAYER

class WallLine:
    lineUp: WallLine
    lineDown: WallLine
    _tileTypes: List[Tile]
    _tilesInLine: List[Optional[Tile]]
    def __init__(self, tileTypesOrder: List[Tile], initialTiles: List[Tile] = [None]*5,
                 lineUp: WallLine = None, lineDown: WallLine = None):
        self._tileTypes = tileTypesOrder.copy()
        self._tilesInLine = initialTiles.copy()
        self._lineUp = lineUp
        self.lineDown = lineDown
        
    def canPutTile(self, tyle: Tile) -> bool:
        return not (tyle in self._tilesInLine or tyle not in self._tileTypes)

    def getTiles(self) -> List[Optional[Tile]]:
        return self._tilesInLine

    def putTile(self, tyle: Tiles) -> Points:
        return #points

    def state(self) -> str:
        return #stringType
