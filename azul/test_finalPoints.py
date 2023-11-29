from finalPointsCalculation import FinalPointsCalculation
from simple_types import Tile, RED, BLACK, BLUE, YELLOW

l = [[RED, RED, BLUE, RED, RED],
     [BLUE, None, None, None, None],
     [BLUE, None, None, None, None],
     [BLUE, None, None, None, None],
     [YELLOW, None, None, None, None]]


print(FinalPointsCalculation.calculate_points(l))