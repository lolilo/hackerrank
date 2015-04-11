from regex import *

number_of_test_cases = int(raw_input())

for test_number in xrange(number_of_test_cases):
    min_length_of_string = int(raw_input())
    regex_expression = raw_input()
    final_number = find_final(min_length_of_string, regex_expression)
    print find_final
