from simple_types import Tile, RED, BLACK, BLUE, YELLOW, GREEN
from random import shuffle
from typing import List
from usedTiles import usedTiles


class Bag:
    _tiles: List[Tile] = []
    
    def __init__(self, used_tiles: usedTiles) -> None:
        self.used_tiles: usedTiles = used_tiles
        for i in range(20):
            self._tiles += [RED, BLACK, BLUE, YELLOW, GREEN]

    def take(self, count: int) -> List[Tile]:
        shuffle(self._tiles)
        
        out: List[Tile] = []

        for i in range(count):
            if len(self._tiles) == 0:
                self.refill()
            out += [self._tiles.pop(-1)]
        
        return out
    
    def refill(self) -> None:
        self._tiles = self.used_tiles.takeAll()

    def state(self) -> str:
        return f"zostava {len(self._tiles)}"