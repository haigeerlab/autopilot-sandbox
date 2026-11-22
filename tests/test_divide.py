import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "src"))

import divide


class DivideTest(unittest.TestCase):
    def test_div(self):
        self.assertEqual(divide.div(6, 3), 2)
        self.assertEqual(divide.div(7, 2), 3.5)
        self.assertEqual(divide.div(-6, 3), -2)

    def test_div_by_zero(self):
        with self.assertRaises(ValueError) as ctx:
            divide.div(1, 0)
        self.assertEqual(str(ctx.exception), "除数不能为 0")


if __name__ == "__main__":
    unittest.main()
