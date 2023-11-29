from __future__ import annotations
from typing import List
from interfaces import UsedTilesGiveInterface
from simple_types import Tile, compress_tile_list, Points, RED, BLUE, YELLOW, GREEN, BLACK, STARTING_PLAYER

class TileSource:
    def __init__(self) -> None:
        self.tiles: list[Tile] = []
    
    def isEmpty(self) -> bool:
        return (self.tiles == [])
    
    def take(self, colour: int) -> list[Tile]:  #RBYGL
        result: list[Tile] = []
        mapColours: dict = {1 : "R", 2 : "B", 3 : "Y", 4 : "G", 5 : "L"}
        i: int = 0
        while i < len(self.tiles):
            if colour < 0: 
                return []
            if mapColours[colour] == self.tiles[i].__str__():
                result.append(self.tiles.pop(i))
            else:
                i += 1
        return result
    
    def state(self) -> str:
        return "".join([str(x) for x in self.tiles])


class tableCenter(TileSource):
    def __init__(self) -> None:
        super().__init__()
        self.tiles = [STARTING_PLAYER]

    def add(self, tiles: list[Tile]) -> None:
        self.tiles += tiles
    
    def take(self, colour: int) -> list[Tile]:  #RBYGL
        result: list[Tile] = []
        mapColours: dict = {0 : "S", 1 : "R", 2 : "B", 3 : "Y", 4 : "G", 5 : "L"}
        i: int = 0
        while i < len(self.tiles):
            if colour < 0: 
                return []
            if self.tiles[i].__str__() == mapColours[colour] or self.tiles[i].__str__() == "S":
                result.append(self.tiles.pop(i))
            else:
                i += 1
        return result