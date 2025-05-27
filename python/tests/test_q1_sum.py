# test_q1_sum.py
import unittest
from python.problems.q1_sum import sum_two_numbers

class TestSum(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(sum_two_numbers(3, 4), 7)
        self.assertEqual(sum_two_numbers(-1, 1), 0)
        self.assertEqual(sum_two_numbers(0, 0), 0)

if __name__ == '__main__':
    unittest.main()
