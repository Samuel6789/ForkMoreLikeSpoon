from __future__ import annotations
from typing import List, Optional
from simple_types import Tile, compress_tile_list, Points, RED, BLUE, YELLOW, GREEN, BLACK, STARTING_PLAYER

class WallLine:
    lineUp: WallLine
    lineDown: WallLine
    _tileTypes: List[Tile]  #order of patterns
    _tilesInLine: List[Optional[Tile]]  #list of Tile and None for missing pattern tiles

    def __init__(self, tileTypesOrder: List[Tile],lineUp: WallLine = None, lineDown: WallLine = None,
                 initialTiles: List[Tile] = [None]*5):   #initialTiles for testing only
        self._tileTypes = tileTypesOrder.copy()
        self._tilesInLine = initialTiles.copy()
        self.lineUp = lineUp
        self.lineDown = lineDown
        
    def canPutTile(self, tyle: Tile) -> bool:
        return not (tyle in self._tilesInLine or tyle not in self._tileTypes)

    def getTiles(self) -> List[Optional[Tile]]:
        return self._tilesInLine

    def putTile(self, tyle: Tiles) -> Points:
        if(not self.canPutTile(tyle)):
            return Points(0)
        
        indexOfTyle: int = self._tileTypes.index(tyle)
        self._tilesInLine[indexOfTyle] = tyle
        
        horizontalPoints: int = 0   #####scoring horizontal
        for offset in range(1, 5):
            indexing: int = indexOfTyle - offset
            if(indexing < 0 or self._tilesInLine[indexing] is None):
                break
            horizontalPoints += 1
        for offset in range(1, 5):
            indexing: int = indexOfTyle + offset
            if(indexing >= 5 or self._tilesInLine[indexing] is None):
                break
            horizontalPoints += 1
        if(horizontalPoints > 0):
            horizontalPoints += 1
            
        verticalPoints: int = 0     #####scoringVertical
        nextWallLine: WallLine = self.lineUp
        for i in range(1, 5):
            if(nextWallLine is None or nextWallLine.getTiles()[indexOfTyle] is None):
                break
            verticalPoints += 1
            nextWallLine = nextWallLine.lineUp
        nextWallLine = self.lineDown
        for i in range(1, 5):
            if(nextWallLine is None or nextWallLine.getTiles()[indexOfTyle] is None):
                break
            verticalPoints += 1
            nextWallLine = nextWallLine.lineDown
        if(verticalPoints > 0):
            verticalPoints += 1
            
        if(verticalPoints + horizontalPoints == 0):
            return Points(1)
        return Points(horizontalPoints + verticalPoints)

    def state(self) -> str:
        tilesInLineNoNone: List[Tile] = [i for i in self._tilesInLine if i is not None]
        #might be better with EMPTY tile, so that it prints empty spaces
        return compress_tile_list(tilesInLineNoNone)
