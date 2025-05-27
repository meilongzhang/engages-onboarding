# test_q3_reverse_string.py
import unittest
from q3_reverse_string import reverse_string

class TestReverse(unittest.TestCase):
    def test_reverse(self):
        self.assertEqual(reverse_string("hello"), "olleh")
        self.assertEqual(reverse_string("a"), "a")
        self.assertEqual(reverse_string(""), "")

if __name__ == '__main__':
    unittest.main()
