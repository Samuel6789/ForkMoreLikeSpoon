from usedTiles import usedTiles
from bag import Bag
from interfaces import UsedTilesGiveInterface

"""
spravit instanciu table area (ta si sama vytvori factory)
"""

class Game:
    _isGameEnd: bool = False
    
    def __init__(self) -> None:
        self.bag = Bag(self.used_tiles)
        # .used_tiles = usedTiles()



    def setEnd(self) -> None:
        self._isGameEnd = True
        self.used_tiles = usedTiles()