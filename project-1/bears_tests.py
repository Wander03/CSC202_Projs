import unittest
from bears import *

# Starter test cases - write more!

class TestAssign1(unittest.TestCase):
    def test_bear_01(self) -> None:
        self.assertTrue(bears(250))

    def test_bear_02(self) -> None:
        self.assertTrue(bears(42))

    def test_bear_03(self) -> None:
        self.assertFalse(bears(53))

    def test_bear_04(self) -> None:
        self.assertFalse(bears(41))

    def test_bear_05(self) -> None:
        self.assertFalse(bears(-42))

    def test_bear_06(self) -> None:
        self.assertFalse(bears(0))

    def test_bear_07(self) -> None:
        self.assertTrue(bears(210))

    def test_bear_08(self) -> None:
        self.assertTrue(bears(1000))

    def test_bear_09(self) -> None:
        self.assertFalse(bears(10000))

    def test_bear_10(self) -> None:
        self.assertFalse(bears(50000))

    def test_bear_11(self) -> None:
        self.assertTrue(bears(2000))

if __name__ == "__main__":
    unittest.main()
