import unittest
from regex import *

class Test(unittest.TestCase):
    def setUp(self):
        pass
    def test_find_smallest_string_length(self):
        regex_expression = 'abc'
        regex_index = 0
        previous_concatenation_length = 501
        current_concatenation_length = 0

        smallest_length = find_smallest_string_length(regex_expression, regex_index, previous_concatenation_length, current_concatenation_length)
        print smallest_length
        self.assertEqual(smallest_length, 3)

if __name__ == "__main__":
    unittest.main()
