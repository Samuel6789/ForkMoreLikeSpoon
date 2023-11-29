import unittest
from bag import Bag


class TestBag(unittest.TestCase):
    def setUp(self) -> None:
        self.bag = Bag("gjh")

    def test(self) -> None:
        self.assertEqual(self.bag.state(), "zostava 100")
        for i in range(100):
            self.bag.take(1)
            self.assertEqual(self.bag.state(), f"zostava {100 - i - 1}")

if __name__ == '__main__':
    unittest.main()
