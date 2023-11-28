from Assignment.azul.simple_types import *
from typing import List
import random


class Bag:
    def __init__(self):
        self.tiles: List[Tile] = []
        for _ in range(20):
            self.tiles.extend([RED, BLUE, YELLOW, GREEN, BLACK])
        pseudorandom = random.Random(555)
        pseudorandom.shuffle(self.tiles)
        print(*self.tiles)

    def state(self) -> str:
        return compress_tile_list(self.tiles)

    def take(self, count: int) -> List[Tile]:
        if count < 0 or count > len(self.tiles):
            return []
        result: List[Tile] = []
        for _ in range(count):
            result.append(self.tiles.pop())
        return result
