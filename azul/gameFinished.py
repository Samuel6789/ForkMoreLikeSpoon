from interfaces import FinishRoundResult
from simple_types import Tile
from typing import List

class GameFinished:
    def __init__(self) -> None:
        pass
    
    def verify(l: List[List[Tile]]) -> FinishRoundResult:
        '''i prefered to make this a function not a class'''
        for row in l:
            if None not in row:
                return FinishRoundResult.GAME_FINISHED
            
        return FinishRoundResult.NORMAL