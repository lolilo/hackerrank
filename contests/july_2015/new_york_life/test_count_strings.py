import unittest
from count_strings import *

import string
import itertools

class RegexTest(unittest.TestCase):
    def setUp(self):
        self.alphabet = set(string.ascii_lowercase)
        self.alphabet_value_array = [0] + [x**2 for x in xrange(1, 27)]

    def test_findsubsets(self):
        subsets = findsubsets(self.alphabet, 2)
        self.assertEqual(len(set(subsets)), 325)

    def test_countStrings(self):
        count = countStrings(2, 13)
        self.assertEqual(count, 2)

if __name__ == "__main__":
    unittest.main()
