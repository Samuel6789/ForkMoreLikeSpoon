from typing import List
from simple_types import Tile, Points

class PatternLine:
    _line = []
    def __init__(self, index: int, floor_line, used_tiles, wall_line) -> None:
        """0: [None], 1:[None, None], ..., 4:[None, None, None, None, None]"""
        self._line = [None for i in range(index + 1)]

    def put(self, tiles: List[Tile]):
        """ak sa nachadza STArting player, tak ho da do floor"""
        pass
        

    def finishRound(self) -> Points:
        pass

    def state() -> str:
        pass

