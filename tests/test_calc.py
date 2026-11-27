import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "src"))

import calc


class CalcTest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(2, 3), 5)

    def test_sub(self):
        self.assertEqual(calc.sub(5, 3), 2)

    def test_mul(self):
        self.assertEqual(calc.mul(3, 4), 12)
        self.assertEqual(calc.mul(5, 0), 0)
        self.assertEqual(calc.mul(-2, 3), -6)


class PowerTest(unittest.TestCase):
    def test_power(self):
        self.assertEqual(calc.power(2, 10), 1024)
        self.assertEqual(calc.power(5, 0), 1)
        self.assertEqual(calc.power(-2, 3), -8)

    def test_negative_exponent(self):
        with self.assertRaises(ValueError):
            calc.power(2, -1)



class ModTest(unittest.TestCase):
    def test_mod(self):
        self.assertEqual(calc.mod(7, 3), 1)
        self.assertEqual(calc.mod(9, 3), 0)

    def test_zero_divisor(self):
        with self.assertRaises(ValueError):
            calc.mod(7, 0)


if __name__ == "__main__":
    unittest.main()
