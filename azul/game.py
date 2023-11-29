from usedTiles import usedTiles
from bag import Bag
from interfaces import UsedTilesGiveInterface
from board import Board
from tableArea import TableArea

"""
spravit instanciu table area (ta si sama vytvori factory)
"""

class Game:
    _isGameEnd: bool = False
    
    
    def __init__(self, num_of_players: int= 2) -> None:
        self.bag = Bag(self.used_tiles)
        self.used_tiles: usedTiles = usedTiles()
        self.boards: Board = [Board(self.used_tiles) for i in range(num_of_players)]
        self.table = [TableArea(num_of_players, self.bag) for i in range(num_of_players)]



    def setEnd(self) -> None:
        self._isGameEnd = True
        self.used_tiles = usedTiles()
    
    # def turns(self) -> None:
    #     while 42:
