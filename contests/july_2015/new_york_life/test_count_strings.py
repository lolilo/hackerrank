import unittest
from count_strings import *

import string
import itertools

class RegexTest(unittest.TestCase):
    def setUp(self):
        self.alphabet = set(string.ascii_lowercase)
        self.alphabet_value_array = [0] + [x**2 for x in xrange(1, 27)]
        # self.alphabet_value_array = [4, 9]
        self.alphabet_value_set = set(self.alphabet_value_array)

    def test_countStrings(self):
        count = countStrings(2, 13)
        self.assertEqual(count, 2)

    def test_get_num_valid_strings(self):
        l = 2
        target_value = 13
        count = get_num_valid_strings(l, target_value, self.alphabet_value_array, self.alphabet_value_set)
        self.assertEqual(count, 2)

if __name__ == "__main__":
    unittest.main()
