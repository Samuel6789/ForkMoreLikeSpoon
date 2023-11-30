from __future__ import annotations
import unittest
from typing import List
from azul.simple_types import Points, Tile, STARTING_PLAYER, RED, BLUE, YELLOW, GREEN, BLACK
from azul.board import Board
from azul.finalPointsCalculation import FinalPointsCalculation
from azul.gameFinished import GameFinished
from azul.interfaces import FinishRoundResult
from azul.usedTiles import usedTiles
from azul.wallLine import WallLine
from azul.floor import Floor

class testBoard(unittest.TestCase):
    def setUp(self) -> None:
        self.used: usedTiles = usedTiles()
        self.board: Board = Board(self.used)

    def test_board(self) -> None:
        self.assertEqual(self.board._floor.state(), "")
        self.assertTrue(len(self.board._wall) == 5)
        self.assertTrue(len(self.board._pattern_line) == 5)
        self.board.put(0, [RED])
        self.assertEqual(self.board._pattern_line[0].state(), "R")
        self.board.finishRound()
        self.assertEqual(self.board.state(), ": has number of points 1")
        self.board.put(0, [BLUE])
        self.board.finishRound()
        self.board.put(0, [YELLOW])
        self.board.finishRound()
        self.board.put(0, [GREEN, GREEN])
        self.board.finishRound()
        self.board.put(0, [BLACK])
        self.assertEqual(self.board.finishRound(), FinishRoundResult.GAME_FINISHED)
        self.assertEqual(self.board.state(),": has number of points 16")
        

if __name__ == '__main__':
    unittest.main()