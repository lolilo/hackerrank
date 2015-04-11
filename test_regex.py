import unittest
from regex import *

class RegexTest(unittest.TestCase):
    def setUp(self):
        self.regex_index = 0
        self.previous_concatenation_length = 501
        self.current_concatenation_length = 0

    def test_find_smallest_string_length_char(self):
        regex_expression = 'abc'
        smallest_length = find_smallest_string_length(regex_expression, self.regex_index, self.previous_concatenation_length, self.current_concatenation_length)
        self.assertEqual(smallest_length, 3)

    def test_find_smallest_string_length_star(self):
        regex_expression = 'abc*'
        smallest_length = find_smallest_string_length(regex_expression, self.regex_index, self.previous_concatenation_length, self.current_concatenation_length)
        self.assertEqual(smallest_length, 2)

    def test_find_smallest_string_length_or1(self):
        regex_expression = 'abc|o'
        smallest_length = find_smallest_string_length(regex_expression, self.regex_index, self.previous_concatenation_length, self.current_concatenation_length)
        self.assertEqual(smallest_length, 1)

    def test_find_smallest_string_length_or2(self):
        regex_expression = 'c|o'
        smallest_length = find_smallest_string_length(regex_expression, self.regex_index, self.previous_concatenation_length, self.current_concatenation_length)
        self.assertEqual(smallest_length, 1)

    def test_find_smallest_string_length_or3(self):
        regex_expression = 'c|odsf'
        smallest_length = find_smallest_string_length(regex_expression, self.regex_index, self.previous_concatenation_length, self.current_concatenation_length)
        self.assertEqual(smallest_length, 1)

    def test_find_smallest_string_length_parenthesis(self):
        regex_expression = 'ab*(c|d)'
        smallest_length = find_smallest_string_length(regex_expression, self.regex_index, self.previous_concatenation_length, self.current_concatenation_length)
        self.assertEqual(smallest_length, 2)

    def test_find_smallest_string_length_parenthesis2(self):
        regex_expression = '(ac|vd)*'
        smallest_length = find_smallest_string_length(regex_expression, self.regex_index, self.previous_concatenation_length, self.current_concatenation_length)
        self.assertEqual(smallest_length, 2)

class PartialRegexTest(unittest.TestCase):
    def setUp(self):
        self.regex_index = 0
        self.previous_concatenation_length = 501
        self.current_concatenation_length = 0

    def test_find_smallest_string_length_char(self):
        regex_expression = 'abc'
        smallest_length = find_smallest_string_length(regex_expression, self.regex_index, self.previous_concatenation_length, self.current_concatenation_length)
        self.assertEqual(smallest_length, 3)

    def test_find_smallest_string_length_star(self):
        regex_expression = 'abc*'
        smallest_length = find_smallest_string_length(regex_expression, self.regex_index, self.previous_concatenation_length, self.current_concatenation_length)
        self.assertEqual(smallest_length, 2)

    def test_find_smallest_string_length_or1(self):
        regex_expression = 'abc|o'
        smallest_length = find_smallest_string_length(regex_expression, self.regex_index, self.previous_concatenation_length, self.current_concatenation_length)
        self.assertEqual(smallest_length, 1)

    def test_find_smallest_string_length_or2(self):
        regex_expression = 'c|o'
        smallest_length = find_smallest_string_length(regex_expression, self.regex_index, self.previous_concatenation_length, self.current_concatenation_length)
        self.assertEqual(smallest_length, 1)

    def test_find_smallest_string_length_or3(self):
        regex_expression = 'c|odsf'
        smallest_length = find_smallest_string_length(regex_expression, self.regex_index, self.previous_concatenation_length, self.current_concatenation_length)
        self.assertEqual(smallest_length, 1)

    def test_find_smallest_string_length_parenthesis(self):
        regex_expression = 'ab*(c|d)'
        smallest_length = find_smallest_string_length(regex_expression, self.regex_index, self.previous_concatenation_length, self.current_concatenation_length)
        self.assertEqual(smallest_length, 2)

    def test_find_smallest_string_length_parenthesis2(self):
        regex_expression = '(ac|vd)*'
        smallest_length = find_smallest_string_length(regex_expression, self.regex_index, self.previous_concatenation_length, self.current_concatenation_length)
        self.assertEqual(smallest_length, 2)

    def test_find_smallest_string_length_parenthesis2(self):
        regex_expression = '(ac|vd)*a*'
        smallest_length = find_smallest_string_length(regex_expression, self.regex_index, self.previous_concatenation_length, self.current_concatenation_length)
        self.assertEqual(smallest_length, 1)  

if __name__ == "__main__":
    unittest.main()
