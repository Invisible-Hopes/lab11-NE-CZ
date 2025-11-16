#https://github.com/Invisible-Hopes/lab11-NE-CZ
#Partner 1 - Nakshatra Elango
#Partner 2 - Chengze Zhao

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    def test_add(self): # 3 assertions
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(3, 4), 7)
        self.assertEqual(add(-1, 1), 0)

    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(3, 2), 1)
        self.assertEqual(subtract(5, 2), 3)
        self.assertEqual(subtract(3, 4), -1)


    def test_multiply(self):
        self.assertEqual(multiply(2,3),6)
        self.assertEqual(multiply(-1,5),-5)
        self.assertEqual(multiply(0,10),0)

    def test_divide(self):
        self.assertEqual(divide(10,2),5)
        self.assertEqual(divide(9,3),3)
        self.assertEqual(divide(7,2),3.5)

    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            divide(0, 5)

    def test_logarithm(self): # 3 assertions
         self.assertEqual(logarithm(3, 9), 2)
         self.assertEqual(logarithm(4, 16), 2)
         self.assertEqual(logarithm(10, 100), 2)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(1, 10)

    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(0, 10)
        with self.assertRaises(ValueError):
            logarithm(1, 10)
        with self.assertRaises(ValueError):
            logarithm(-2, 5)

    def test_hypotenuse(self): # 3 assertions
        self.assertAlmostEqual(hypotenuse(3,4), 5)
        self.assertAlmostEqual(hypotenuse(5,12), 13)
        self.assertAlmostEqual(hypotenuse(-6,-8), 10)

    def test_sqrt(self): # 3 assertions
        self.assertAlmostEqual(square_root(4), 2)
        self.assertAlmostEqual(square_root(0), 0)
        with self.assertRaises(ValueError):
            square_root(-1)

if __name__ == "__main__":
    unittest.main()
