# test_q6_multiplication_table.py
import unittest
from q6_multiplication_table import multiplication_table

class TestMultiples(unittest.TestCase):
    def test_table(self):
        self.assertEqual(multiplication_table(2), [2, 4, 6, 8, 10, 12, 14, 16, 18, 20])

if __name__ == '__main__':
    unittest.main()
