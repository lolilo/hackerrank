from regex import *

number_of_test_cases = int(raw_input())

for test_number in xrange(number_of_test_cases):
    min_length_of_string = int(raw_input())
    regex_expression = raw_input()

    regex_index = 0
    previous_concatenation_length = 501
    current_concatenation_length = 0
    
    smallest_possible_string_length = find_smallest_string_length(regex_expression, regex_index, previous_concatenation_length, current_concatenation_length)
    
    if smallest_possible_string_length < min_length_of_string:
        smallest_possible_string_length = extend_by_smallest()

    print smallest_possible_string_length

