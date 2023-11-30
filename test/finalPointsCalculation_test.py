from __future__ import annotations
import unittest
from azul import finalPointsCalculation
from azul.simple_types import *


class SpravnostBodovania(unittest.TestCase):
    def test_iba_stlpce(self):
        f = finalPointsCalculation.FinalPointsCalculation()
        wall = [[BLUE, None, None, None, None],
                [GREEN, None, None, None, None],
                [BLACK, None, None, None, None],
                [RED, None, None, None, None],
                [YELLOW, None, None, None, None]]
        self.assertEqual('7', str(f.calculate_points(wall)))

    def test_iba_riadky(self):
        f = finalPointsCalculation.FinalPointsCalculation()
        wall = [[BLUE, YELLOW, RED, BLACK, GREEN],
              [None, None, None, None, None],
              [None, None, None, None, None],
              [None, None, None, None, None],
              [None, None, None, None, None]]
        self.assertEqual('2', str(f.calculate_points(wall)))

    def test_prazdneho_wall(self):
        f = finalPointsCalculation.FinalPointsCalculation()
        wall = 5 * [[None]*5]
        self.assertEqual('0', str(f.calculate_points(wall)))

    def test_z_kazdeho_nieco(self):
        f = finalPointsCalculation.FinalPointsCalculation()
        wall = [[BLUE, YELLOW, RED, None, None],
                [GREEN, BLUE, YELLOW, None, None],
                [BLACK, None, BLUE, YELLOW, RED],
                [RED, BLACK, None, BLUE, None],
                [YELLOW, RED, BLACK, GREEN, BLUE]]
        self.assertEqual('19', str(f.calculate_points(wall)))

    def test_plny_wall(self):
        f = finalPointsCalculation.FinalPointsCalculation()
        wall = [[BLUE, YELLOW, RED, BLACK, GREEN],
                [GREEN, BLUE, YELLOW, RED, BLACK],
                [BLACK, GREEN, BLUE, YELLOW, RED],
                [RED, BLACK, GREEN, BLUE, YELLOW],
                [YELLOW, RED, BLACK, GREEN, BLUE]]
        self.assertEqual(str(5 * (2 + 7 + 10)), str(f.calculate_points(wall)))


if __name__ == '__main__':
    unittest.main()
