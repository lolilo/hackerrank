# refactor out min_length_of_string later
# keep track of shortest extender as we parse? optimize later
def find_smallest_string_length(regex_expression, regex_index, previous_concatenation_length, current_concatenation_length):

    if regex_index >= len(regex_expression): # reached end of regex pattern
        return 0

    char = regex_expression[regex_index]
    if ord('a') <= ord(char) <= ord('z'):
        current_concatenation_length += 1
        regex_index += 1
        return 1 + find_smallest_string_length(regex_expression, regex_index, previous_concatenation_length, current_concatenation_length)

    elif char == '*':
        chars_that_star_applies_to = 1
        if (regex_index - 1 > 0) and (regex_expression[regex_index - 1] == ')'):
            chars_that_star_applies_to = current_concatenation_length
        current_concatenation_length = 0
        regex_index += 1
        return (- chars_that_star_applies_to) + find_smallest_string_length(regex_expression, regex_index, previous_concatenation_length, current_concatenation_length)

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
        current_concatenation_length += find_smallest_string_length(regex_expression, regex_index, new_previous_concatenation_length, new_current_concatenation_length)
        return current_concatenation_length

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
    current_min_lenth = 501

    while regex_index < length_regex_expression:
        char = regex_expression[regex_index]
        print 'char in while', char
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
        regex_index += 1

    return current_min_length


def find_final(min_length_of_string, regex_expression):
    regex_index_for_search = 0
    previous_concatenation_length = 501
    current_concatenation_length = 0
    current_min_length = find_smallest_string_length(regex_partial_to_search, regex_index_for_search, previous_concatenation_length, current_concatenation_length)
    if current_min_lenth < min_length_of_string:
        smallest_increment = find_smallest_partial(regex_expression)
        while current_min_length < min_length_of_string:
            current_min_length += smallest_increment
    return current_min_length
