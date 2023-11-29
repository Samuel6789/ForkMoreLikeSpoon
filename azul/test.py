from board import Board
# from interfaces import UsedTilesGiveInterface
from simple_types import Tile, RED
from usedTiles import usedTiles

us_tiles = usedTiles()

t = Board(us_tiles)

t._floor.put([RED])

t._floor.finish_round()
print(t.used_tiles.state())