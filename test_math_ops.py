import unittest
from math_ops import subtract

class TestMathOps(unittest.TestCase):
    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(10, 20), -10)
        self.assertEqual(subtract(0, 0), 0)
        self.assertEqual(subtract(-5, -5), 0)

if __name__ == '__main__':
    unittest.main()
