from __future__ import annotations
from typing import List
from tileSources import tableCenter
from factory import Factory
from simple_types import Tile
from bag import Bag

class TableArea:
    def __init__(self, numOfPlayers: int, bag: Bag) -> None:
        self.tableCenter: tableCenter = tableCenter()
        self.factories: List[Factory] = list()
        for i in range (1 + numOfPlayers*2):
            self.factories.append(Factory(bag, self.tableCenter))

    def take(self, sourceIdx: int, colour: int) -> List[Tile]:
        if sourceIdx >= len(self.factories):
            raise ValueError("Invalid source index")
        
        source = self.factories[sourceIdx] if sourceIdx != -1 else self.tableCenter
        return source.take(colour)

    def isRoundEnd(self) -> bool:
        return all(factory.isEmpty() for factory in self.factories) and self.tableCenter.isEmpty()

    def startNewRound(self) -> None:
        for factory in self.factories:
            factory.startNewRound()

    def state(self) -> str:
        factories_state: str = ' '.join([f.state() for f in self.factories])
        center_state: str = self.tableCenter.state()
        return f"Factories: {factories_state} | Center: {center_state}"