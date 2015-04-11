

# refactor out min_length_of_string later
# keep track of shortest extender as we parse? optimize later
def find_smallest_string_length(regex_expression, regex_index, previous_concatenation_length, current_concatenation_length):
    # smallest_string_length = 0 

    if regex_index >= len(regex_expression): # reached end of regex pattern
        print 'herei am'
        return 0

    char = regex_expression[0]

    if ord('a') <= ord(char) <= ord('z'):
        regex_index += 1
        return 1 + find_smallest_string_length(regex_expression, regex_index, previous_concatenation_length, current_concatenation_length)
        print 'in ord', current_concatenation_length

    # elif char == '*':
    #     current_concatenation_length = 0

    # elif char == '|': 
    #     if previous_concatenation_length > current_concatenation_length:
    #         previous_concatenation_length = current_concatenation_length
    #     current_concatenation_length = 0 # restart counter and check the other 'or' regex length

    # elif char == '(':
    #     new_previous_concatenation_length = 501
    #     new_current_concatenation_length = 0
    #     current_concatenation_length += find_smallest_string_length(regex_expression, regex_index + 1, new_previous_concatenation_length, new_current_concatenation_length)

    # elif char == ')':
    #     return min(previous_concatenation_length, current_concatenation_length)

    regex_index += 1

    # smallest_string_length = min(previous_concatenation_length, current_concatenation_length)
    
    return find_smallest_string_length(regex_expression, regex_index, previous_concatenation_length, current_concatenation_length)
    
    print 'current_concatenation_length', current_concatenation_length
    return current_concatenation_length

