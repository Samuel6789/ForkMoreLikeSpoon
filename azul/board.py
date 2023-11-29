from typing import List
from azul.simple_types import Points, Tile, STARTING_PLAYER
import pattern_line
import floor
from interfaces import UsedTilesGiveInterface, FinalPointsCalculationInterface, FinishRoundResult
import wall_line
from game import Game
from game_finished import gameFinished

class Board:
    _points: Points = Points(0)
    _is_first: bool = False        # indicates 
    _wall = [wall_line.WallLine([]) for i in range(5)]        # instancie wall line
    _floor = floor.Floor([], UsedTilesGiveInterface)
    _player_name: str = ""
    _pattern_line: List[pattern_line.PatternLine] = [pattern_line.PatternLine(i) for i in range(4)]

    def __init__(self, player_name: str = "") -> None:
        self._player_name = player_name
    
    def finishRound(self):
        '''zavola finish round z patternline a zapocita vratene body'''
        for line in self._pattern_line:
            self._points = Points.sum(line.finishRound(), self._points)

        if gameFinished() == FinishRoundResult.GAME_FINISHED:
            self.endGame()
            return FinishRoundResult.GAME_FINISHED
        
        return FinishRoundResult.NORMAL

        
    def put(self, destinationIdx: int, tiles: List[Tile]) -> None:
        if not 0 <= destinationIdx <= 4:        #wrong destinationIdx or equal to 5 -> floor
            self._floor.put(tiles)

        if tiles == []:     #uz nie je co vybrat => koncim kolo
            self._is_first = False
            self.finishRound()
        elif STARTING_PLAYER in tiles:     #5 je floor index
            self._is_first = True;
            self._floor.put([STARTING_PLAYER])      #for some reason we chose to do it this way
            tiles = tiles.remove(STARTING_PLAYER)
            self._pattern_line[destinationIdx].put(tiles)
        else:
            self._is_first = False
            self._pattern_line[destinationIdx].put(tiles)

    def endGame(self) -> None:
        self._points = Points.sum(FinalPointsCalculationInterface.getPoints(), self._points)

    def state(self) -> str:
        """vypise kolko bodov ma dany hrac"""
        out = f"{self._player_name}: has number of points {str(self._points)}"
    
    
