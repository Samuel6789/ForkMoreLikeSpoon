from bag import Bag
from tileSources import TileSource, tableCenter
from simple_types import Tile

class Factory(TileSource):
    def __init__(self, bag: Bag, table_center: tableCenter) -> None:
        self._bag = bag
        self.table_center = tableCenter
        super.__init__()
    
    def startNewRound(self) -> None:
        self.tiles = self._bag.take(4)

    def take(self, colour: int) -> list[Tile]:
        self.center.add(self.tiles)
        self.tiles.clear()
        return super().take(colour)
    
