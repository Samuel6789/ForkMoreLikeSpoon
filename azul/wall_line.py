from __future__ import annotations
from typing import List, Optional
from azul.simple_types import Tile, Points, RED, BLUE, YELLOW, GREEN, BLACK, STARTING_PLAYER

class WallLine:
    lineUp: WallLine
    lineDown: WallLine
    _tileTypes: List[Tile]  #order of patterns
    _tilesInLine: List[Optional[Tile]]  #list of Tile and None for missing pattern tiles

    def __init__(self, tileTypesOrder: List[Tile],lineUp: WallLine = None, lineDown: WallLine = None,
                 initialTiles: List[Tile] = list()):   #initialTiles for testing only
        self._tileTypes = tileTypesOrder.copy()     #I assume correct input, no tests
        self.lineUp = lineUp
        self.lineDown = lineDown
        self._tilesInLine = [None]*len(self._tileTypes)
        for initTile in initialTiles:
            self.putTile(initTile)
        
    def canPutTile(self, tyle: Tile) -> bool:
        return not (tyle in self._tilesInLine or tyle not in self._tileTypes)

    def getTiles(self) -> List[Optional[Tile]]:
        return self._tilesInLine

    def putTile(self, tyle: Tiles) -> Points:
        if(not self.canPutTile(tyle)):
            return Points(0)
        
        indexOfTyle: int = self._tileTypes.index(tyle)
        lineSize: int = len(self._tileTypes)
        self._tilesInLine[indexOfTyle] = tyle
        
        horizontalPoints: int = 0   #####scoring horizontal
        for offset in range(1, lineSize):
            indexing: int = indexOfTyle - offset
            if(indexing < 0 or self._tilesInLine[indexing] is None):
                break
            horizontalPoints += 1
        for offset in range(1, lineSize):
            indexing: int = indexOfTyle + offset
            if(indexing >= lineSize or self._tilesInLine[indexing] is None):
                break
            horizontalPoints += 1
        if(horizontalPoints > 0):
            horizontalPoints += 1
            
        verticalPoints: int = 0     #####scoringVertical
        nextWallLine: WallLine = self.lineUp
        for i in range(1, lineSize):
            if(nextWallLine is None or nextWallLine.getTiles()[indexOfTyle] is None):
                break
            verticalPoints += 1
            nextWallLine = nextWallLine.lineUp
        nextWallLine = self.lineDown
        for i in range(1, lineSize):
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
        tilesInLineToStr: List[str] = ['-' if t is None else str(t) for t in self._tilesInLine]
        return "".join(tilesInLineToStr)

        
