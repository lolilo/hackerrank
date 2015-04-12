# refactor out min_length_of_string later
# keep track of shortest extender as we parse? optimize later
def find_smallest_string_length(regex_expression, regex_index, previous_concatenation_length, current_concatenation_length):

    if regex_index >= len(regex_expression): # reached end of regex pattern
        return 0

    char = regex_expression[regex_index]
    if char == ')':
        regex_index += 1
    if ord('a') <= ord(char) <= ord('z'):
        current_concatenation_length += 1
        regex_index += 1
        return 1 + find_smallest_string_length(regex_expression, regex_index, previous_concatenation_length, current_concatenation_length)

    elif char == '*':
        chars_that_star_applies_to = 1
        if (regex_index - 1 > 0) and (regex_expression[regex_index - 1] == ')'):
            chars_that_star_applies_to = 0
        current_concatenation_length -= chars_that_star_applies_to
        regex_index += 1

        return ( - chars_that_star_applies_to) + find_smallest_string_length(regex_expression, regex_index, previous_concatenation_length, current_concatenation_length)

    elif char == '|': 
        if previous_concatenation_length > current_concatenation_length:
            previous_concatenation_length = current_concatenation_length
        placeholder = current_concatenation_length
        current_concatenation_length = 0 # restart counter and check the other 'or' regex length
        regex_index += 1
        current_concatenation_length = find_smallest_string_length(regex_expression, regex_index, previous_concatenation_length, current_concatenation_length)

        return min(previous_concatenation_length, current_concatenation_length) - max(previous_concatenation_length, placeholder)

    elif char == '(':
        new_previous_concatenation_length = 501
        new_current_concatenation_length = 0
        regex_index += 1

        additional_length = find_smallest_string_length(regex_expression, regex_index, new_previous_concatenation_length, new_current_concatenation_length)

        current_concatenation_length += additional_length

        while char != ')':
            regex_index += 1
            char = regex_expression[regex_index]

        regex_index += 1
        return additional_length + find_smallest_string_length(regex_expression, regex_index, previous_concatenation_length, current_concatenation_length)

    elif char == ')':
        return current_concatenation_length

def find_matching_paren_index(string):
    index = len(string) - 1
    while index >= 0:
        if string[index] == '(':
            return index
        index -= 1
    # assume there is always a match 

def find_smallest_partial(regex_expression):
    regex_set = set(regex_expression)
    if '*' not in regex_set:
        return -1

    regex_index = 0
    length_regex_expression = len(regex_expression)
    best_min_length = 1000

    while regex_index < length_regex_expression:
        char = regex_expression[regex_index]
        if char == '*':
            if (regex_index - 1 >= 0):
                prev_char = regex_expression[regex_index - 1]
                if prev_char == ')':
                    regex_partial_to_search = regex_expression[:regex_index - 2]
                    matching_paren_index = find_matching_paren_index(regex_partial_to_search)
                    regex_partial_to_search = regex_expression[matching_paren_index:regex_index]

                    regex_index_for_search = 0
                    previous_concatenation_length = 501
                    current_concatenation_length = 0
                    current_min_length = find_smallest_string_length(regex_partial_to_search, regex_index_for_search, previous_concatenation_length, current_concatenation_length)
                else:
                    current_min_length = 1
            best_min_length = min(current_min_length, best_min_length)
        regex_index += 1

    return best_min_length


def find_final(min_length_of_string, regex_expression):
    if regex_expression[0] == '(' and regex_expression[-1] == '*' and regex_expression[-2] == ')':
        current_min_length = 0
    else:
        regex_index_for_search = 0
        previous_concatenation_length = 501
        current_concatenation_length = 0
        current_min_length = find_smallest_string_length(regex_expression, regex_index_for_search, previous_concatenation_length, current_concatenation_length)

    if current_min_length < min_length_of_string:
        smallest_increment = find_smallest_partial(regex_expression)
        if smallest_increment == -1:
            return -1

        print 'this should only print once ever'
        while current_min_length < min_length_of_string:
            current_min_length += smallest_increment
            print '\nyo'
            print 'increment', smallest_increment
            print current_min_length

    return current_min_length


if __name__ == "__main__":
    number_of_test_cases = int(raw_input())

    for test_number in xrange(number_of_test_cases):
        min_length_of_string = int(raw_input())
        regex_expression = raw_input()
        final_number = find_final(min_length_of_string, regex_expression)
        print final_number
