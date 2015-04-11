def find_smallest_string_legnth(min_length_of_string, regex_expression):
    smallest_string_length = 0
    previous_concatenation_length = 501
    current_concatenation_length = 0
    
    for char in regex_expression:
        if ord('a') <= ord(char) <= ord('z'):
            current_concatenation_length += 1
        
        if char == '*':
            current_concatenation_length = 0

        if char == '|': 
            if previous_concatenation_length > current_concatenation_length:
                previous_concatenation_length = current_concatenation_length
            current_concatenation_length = 0

        if char == '(':
            current_concatenation_length = find_smallest_string_legnth(min_length_of_string, regex_expression)

        if char == ')':
            return min(previous_concatenation_length, current_concatenation_length)

    smallest_string_length = min(previous_concatenation_length, current_concatenation_length)
    
    if smallest_string_length < min_length_of_string:
        length_smallest_extender = find_length_smallest_extender(regex_expression)
        while smallest_string_length < min_length_of_string:
            smallest_string_length += length_smallest_extender

    return smallest_string_length


number_of_test_cases = int(raw_input())

for test_number in xrange(number_of_test_cases):
    min_length_of_string = int(raw_input())
    regex_expression = raw_input()
    print find_smallest_string_legnth(min_length_of_string, regex_expression)
