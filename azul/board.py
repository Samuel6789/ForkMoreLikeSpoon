from typing import List
from simple_types import Points, Tile, STARTING_PLAYER
from pattern_line import PatternLine
from floor import Floor
from interfaces import FinalPointsCalculationInterface, FinishRoundResult#, UsedTilesGiveInterface
from wall_line import WallLine
# from game import Game
from game_finished import gameFinished


class Board:
    _points: Points = Points(0)
    _is_first: bool = False        # indicates 
    _wall = [WallLine([]) for i in range(5)]        # instancie wall line
    
    _player_name: str = ""
    _pattern_line: List[PatternLine] = [PatternLine(i) for i in range(4)]

    def __init__(self, used_tiles, player_name: str = "") -> None:
        self._player_name = player_name
        self.used_tiles = used_tiles
        self._floor = Floor([Points(i) for i in [1, 1, 2, 2]], used_tiles)
    
    def finishRound(self) -> FinishRoundResult:
        '''zavola finish round z patternline a zapocita vratene body'''
        # for line in self._pattern_line:
        #     self._points = Points.sum([line.finishRound(), self._points])

        minus_points = self._floor.finish_round()
        self._points = Points.sum([minus_points, self._points])

        if gameFinished([wl.getTiles() for wl in self._wall]) == FinishRoundResult.GAME_FINISHED:
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
        self._points = Points.sum([FinalPointsCalculationInterface.getPoints(), self._points])

    def state(self) -> str:
        """vypise kolko bodov ma dany hrac"""
        out = f"{self._player_name}: has number of points {str(self._points)}"
