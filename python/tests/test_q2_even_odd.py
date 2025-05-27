# test_q2_even_odd.py
import unittest
from python.problems.q2_even_odd import is_even

class TestEvenOdd(unittest.TestCase):
    def test_even_odd(self):
        self.assertTrue(is_even(2))
        self.assertFalse(is_even(3))
        self.assertTrue(is_even(0))

if __name__ == '__main__':
    unittest.main()
