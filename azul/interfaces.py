from __future__ import annotations
from typing import List, Set, Any
from simple_types import Tile, Points
from enum import Enum
# from usedTiles import usedTiles
# from game import Game


# class UsedTilesGiveInterface:
#     used_tiles: usedTiles = usedTiles()
#     def give(self, tiles: List[Tile]) -> None:
#         print("joooj zavolali ma!!!!!!!!!!!!!!!!!!1")
#         self.used_tiles.give(tiles)
        
class GameInterface:
    ''''''

    def __init__(self) -> None:
        pass

class ObserverInterface:
    '''perposiela observerom state z board-u'''
    def __init__(self) -> None:
        '''prepares GUI in a GUI implementation'''
        self._observers: Set[str] = set()
        pass

    def notify(self, newState:str) -> None:
        '''in a GUI implementation this would pop up a window with a message'''
        print(f"new state is: {newState}")

    def registerObserver(self, name: str) -> None:
        self._observers.add(name)

    def cancelObserver(self, name: str) -> None:
        self._observers.remove(name)

# class FinalPointsCalculationInterface:
#     def getPoints(wall: List[List[Any]]) -> Points:
#         out: Points = Points(0)
#         ...     # TODO pri integracii sem pridat nazov funkcie z realnej classy
#         return out

class FinishRoundResult(Enum):
    NORMAL = True
    GAME_FINISHED = False