def populate_table(l, value, array):
    table = [None for x in xrange(value + 1)]
    table[0] = [[]]
    for i in xrange(1, value+1):
        for num in array:
            if num > i:
                break # numbers are sorted asending
            else:
                if table[i-num] != None:
                    new_combination_pairs = table[i-num][:]
                    for new_combination in new_combination_pairs:
                        to_add = new_combination + [num]
                        len_to_add = len(to_add)
                        if (i < value and len_to_add <= l) or (i == value and len_to_add == l):
                            if table[i] == None:
                                table[i] = [to_add]
                            else:
                                table[i].append(to_add)

    combinations = table[value]
    return len(combinations)

def countStrings(l, v):
    alphabet_value_array = [x**2 for x in xrange(1, 27)]
    return populate_table(l, v, alphabet_value_array)

print countStrings(3, 29)
