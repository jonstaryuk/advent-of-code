import unittest
from day6 import *


class TestDay5(unittest.TestCase):
    def test1(self):
        grid = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        turn_on([1, 2], [3, 3], grid)
        expectedGrid = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 1, 1, 1],
            [0, 1, 1, 1]
        ]
        self.assertEqual(grid, expectedGrid)


if __name__ == '__main__':
    unittest.main()
