# test_q4_max_list.py
import unittest
from python.problems.q4_max_list import find_max

class TestFindMax(unittest.TestCase):
    def test_max(self):
        self.assertEqual(find_max([1, 2, 3]), 3)
        self.assertEqual(find_max([-1, -5, -3]), -1)
        self.assertEqual(find_max([7]), 7)

if __name__ == '__main__':
    unittest.main()
