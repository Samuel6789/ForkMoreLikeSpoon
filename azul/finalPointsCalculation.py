from collections import Counter
from azul.simple_types import Points, Tile
from typing import List, Any


class FinalPointsCalculation:
    @staticmethod
    def calculate_points(wall: List[List[Any]]) -> Points:
        points: int = 0
        colours_counter: Counter[Any] = Counter()
        for row in wall:
            colours_counter.update(row)
            if len(list(map(lambda x: str(x), list(filter(lambda x: x is not None, row))))) == 5:
                points += 2
        for column in zip(*wall):
            if len(list(filter(lambda x: x is not None, column))) == 5:
                points += 7
        del colours_counter[None]
        for count in colours_counter.values():
            if count == 5:
                points += 10
        return Points(points)
