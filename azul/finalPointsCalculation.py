from collections import Counter
from azul.simple_types import Points
from typing import List, Any


class FinalPointsCalculation:
    @staticmethod
    def calculate_points(wall: List[List[Any]]):
        points: int = 0
        colours_counter: Counter = Counter()
        for row in wall:
            row: List[str] = list(filter(lambda x: x is not None, row))
            row: List[str] = list(map(lambda x: str(x), row))
            colours_counter.update(row)
            if len(row) == 5:
                points += 2
        for column in zip(*wall):
            column: List[str] = list(filter(lambda x: x is not None, column))
            if len(column) == 5:
                points += 7
        del colours_counter[None]
        for count in colours_counter.values():
            if count == 5:
                points += 10
        return Points(points)
