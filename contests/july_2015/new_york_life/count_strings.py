def populate_table(l, value, array):
    table = [None for x in xrange(value + 1)]
    table[0] = [0]
    for i in xrange(1, value+1):
        for num in array:
            if num > i:
                print num
                break # numbers are sorted asending
            else:
                if table[i-num] != None:
                    num_possible_add_ons = table[i-num] # list of lengths
                    for length in num_possible_add_ons:
                        len_to_add = length + 1
                        if (i < value and len_to_add < l) or (i == value and len_to_add == l):
                            if table[i] == None:
                                table[i] = [len_to_add]
                            else:
                                table[i].append(len_to_add)

    combinations = table[value]
    return len(combinations) % 10000007

def countStrings(l, v):
    alphabet_value_array = [x**2 for x in xrange(1, 27)]
    return populate_table(l, v, alphabet_value_array)

print countStrings(3, 29)
