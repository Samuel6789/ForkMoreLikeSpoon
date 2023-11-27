from __future__ import annotations
from typing import List
from itertools import chain, repeat, islice
from interfaces import UsedTilesGiveInterface
from simple_types import Tile, Points #, compress_tile_list

class WallLine:
    lineUp: WallLine
    lineDown: WallLine
    _tileTypes: List[Tile]
    def __init__(self, lineUp: WallLine = None, lineDown: WallLine = None, initialTiles: List[Tile] = list()):
        self._tileTypes = list()
        for initTile in initialTiles:
            if(str(initTile) in _tileTypes):
                self._tileTypes.append(str(initTile)) #ukladam str v tomto commite
            self._lineUp = lineUp
            self.lineDown = lineDown
        
    def canPutTile(tyle: Tile) -> bool:
        if (str(tyle) in self._tileTypes): #ukladat str alebo tile alebo co?
            return False
        return True

def getTiles(tyle: Tile) -> None:
    pass

def putTile(tyle: Tiles) -> Points:
    return #points

def state() -> str:
    return #stringType
