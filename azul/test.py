from board import Board
from interfaces import UsedTilesGiveInterface
from simple_types import Tile, RED


t = Board(used_tiles=UsedTilesGiveInterface.used_tiles)

t._floor.put([RED])

t._floor.finish_round()

print(UsedTilesGiveInterface.used_tiles.state())

# t.put(5, [Tile()])