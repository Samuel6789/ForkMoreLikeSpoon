from __future__ import annotations
from typing import List
from simple_types import Tile, compress_tile_list, Points, RED, BLUE, YELLOW, GREEN, BLACK

class usedTiles():
    def __init__(self) -> None:
        self.tiles: List[Tile] = []
    
    def state(self) -> str:
        return "".join([str(x) for x in self.tiles])
    
    def give(self, tiles: List[Tile]) -> None:
        for tile in tiles: 
            if tile.__str__() != "S":
                self.tiles.append(tile)
        
    def takeAll(self) -> list[Tile]:
        result: List[Tile] = self.tiles
        self.tiles = []
        return result