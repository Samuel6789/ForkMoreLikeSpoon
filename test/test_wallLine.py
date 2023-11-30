from __future__ import annotations
import unittest
from typing import List, Optional
from azul.simple_types import Tile, STARTING_PLAYER, RED, BLUE, YELLOW, GREEN, BLACK, Points
from azul.wallLine import WallLine

class TestWallLine(unittest.TestCase):
    def setUp(self) -> None:
        self.fake_wall = []
        patternOrder: List[Tile] = [RED, BLUE, YELLOW, GREEN, BLACK]
        size = len(patternOrder)
        for i in range(size):
            shift: int = (size - i)%size
            shiftedPatterns = patternOrder[shift:] + patternOrder[:shift]
            self.fake_wall.append(WallLine(shiftedPatterns))
        for j in range(size):
            if(j > 0):
                self.fake_wall[j].lineUp = self.fake_wall[j - 1]
            if(j < size - 1):
                self.fake_wall[j].lineDown = self.fake_wall[j + 1]
        self.wall_line = self.fake_wall[3]

    def test_tiles(self) -> None:
        self.assertCountEqual(self.wall_line.state(), "-----")
        get_tiles: List[Optional[Tile]] = self.wall_line.getTiles()
        self.assertCountEqual(get_tiles, [None, None, None, None, None])
        self.assertIs(self.wall_line.canPutTile(GREEN), True)
        self.assertIs(self.wall_line.canPutTile(STARTING_PLAYER), False)
        points: Points = self.wall_line.putTile(GREEN)
        self.assertCountEqual(str(points), "1")
        self.assertCountEqual(self.wall_line.state(), "-G---")
        get_tiles2: List[Optional[Tile]] = self.wall_line.getTiles()
        self.assertCountEqual(get_tiles2, [None, GREEN, None, None, None])
        self.wall_line.lineUp.putTile(BLUE)
        self.wall_line.lineDown.putTile(BLACK)
        points2: Points = self.wall_line.putTile(RED)
        self.assertCountEqual(str(points2), "3")
        self.wall_line.lineUp.putTile(RED)
        self.wall_line.lineDown.putTile(GREEN)
        points3: Points = self.wall_line.putTile(BLACK)
        self.assertCountEqual(str(points3), "6")
        self.assertIs(self.wall_line.canPutTile(BLACK), False)
        points4: Points = self.wall_line.putTile(BLACK)
        self.assertCountEqual(str(points4), "0")
        self.assertCountEqual(self.wall_line.state(), "-GLR-")
        get_tiles3: List[Optional[Tile]] = self.wall_line.getTiles()
        self.assertCountEqual(get_tiles3, [None, GREEN, BLACK, RED, None])   

if __name__ == '__main__':
    unittest.main()
