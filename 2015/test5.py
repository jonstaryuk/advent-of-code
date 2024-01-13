import unittest
from day5part2 import *


class TestDay5(unittest.TestCase):
    def test1(self):
        self.assertTrue(contains_repeated_letter_pairs("qjhvhtzxzqqjkmpb"))
        self.assertTrue(contains_sandwich("qjhvhtzxzqqjkmpb"))
        self.assertTrue(is_nice("qjhvhtzxzqqjkmpb"))

    def test2(self):
        self.assertTrue(contains_repeated_letter_pairs("xxyxx"))
        self.assertTrue(contains_sandwich("xxyxx"))
        self.assertTrue(is_nice("xxyxx"))

    def test3(self):
        self.assertTrue(contains_repeated_letter_pairs("uurcxstgmygtbstg"))
        self.assertFalse(contains_sandwich("uurcxstgmygtbstg"))
        self.assertFalse(is_nice("uurcxstgmygtbstg"))

    def test4(self):
        self.assertFalse(contains_repeated_letter_pairs("ieodomkazucvgmuy"))
        self.assertTrue(contains_sandwich("ieodomkazucvgmuy"))
        self.assertFalse(is_nice("ieodomkazucvgmuy"))

    def test4(self):
        self.assertFalse(contains_repeated_letter_pairs("asdfijkfff"))
        self.assertTrue(contains_repeated_letter_pairs("asdfijkffsff"))
        self.assertTrue(contains_repeated_letter_pairs("asdfijkffff"))
        self.assertFalse(contains_repeated_letter_pairs("rmmmqkr"))

if __name__ == '__main__':
    unittest.main()
