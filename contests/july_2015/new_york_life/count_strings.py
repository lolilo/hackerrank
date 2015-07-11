# Complete the function below.

def get_num_valid_strings(l, target_value, alphabet_value_array, alphabet_value_set):
    if l < 1 and target_value > 0:
        return 0

    if l == 0 and target_value == 0:
        return 1

    count = 0
    for value in alphabet_value_array:
        remaining_value = target_value - value
        if remaining_value in alphabet_value_set: # this is wrong. We need to see if there exists numbers that add up to remaining value
            count += get_num_valid_strings(l - 1, target_value - value, alphabet_value_array, alphabet_value_set)
    return count

def countStrings(l, v):
    alphabet_value_array = [0] + [x**2 for x in xrange(1, 27)]
    alphabet_value_set = set(alphabet_value_array)
    return get_num_valid_strings(l, v, alphabet_value_array, alphabet_value_set)

count = countStrings(2, 13)
print count
