from usedTiles import usedTiles
from bag import Bag

"""
spravit instanciu table area (ta si sama vytvori factory)


"""

class Game:
    _isGameEnd: bool = False

    def __init__(self) -> None:
        self.bag = Bag(self.used_tiles)
        self.used_tiles: usedTiles = usedTiles()
        

    def setEnd(self) -> None:
        self._isGameEnd = True
        self.used_tiles = usedTiles()