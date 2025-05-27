# test_q5_count_vowels.py
import unittest
from q5_count_vowels import count_vowels

class TestCountVowels(unittest.TestCase):
    def test_count(self):
        self.assertEqual(count_vowels("hello"), 2)
        self.assertEqual(count_vowels("sky"), 0)
        self.assertEqual(count_vowels("AEIOU"), 5)

if __name__ == '__main__':
    unittest.main()
