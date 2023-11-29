from interfaces import FinishRoundResult
from simple_types import Tile
from typing import List


def gameFinished(l: List[List[Tile]]) -> FinishRoundResult:
    '''i prefered to make this a function not a class'''
    
    return FinishRoundResult.NORMAL