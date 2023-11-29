from collections import Counter
from simple_types import Points
from typing import List, Any


class FinalPointsCalculation:
    @staticmethod
    def calculate_points(wall: List[List[Any]]) -> Points:
        points: int = 0
        colours_counter: Counter = Counter()
        for row in wall:
            row = list(filter(lambda x: x is not None, row))
            row = list(map(lambda x: str(x), row))
            colours_counter.update(row)
            if len(row) == 5:
                points += 2
        for column in zip(*wall):
            column = tuple(filter(lambda x: x is not None, list(column)))
            if len(column) == 5:
                points += 7
        del colours_counter[None]
        for count in colours_counter.values():
            if count == 5:
                points += 10
        return Points(points)