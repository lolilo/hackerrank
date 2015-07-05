def get_two_strings(s, mid):
    s1 = s[:mid]
    s2 = s[mid:]
    return s1, s2

def get_dict(s):
    d = {}
    for char in s:
        if d.get(char):
            d[char] += 1
        else:
            d[char] = 1
    return d

def sum_different_dict_values(dict):
    total = 0
    for key in dict.keys():
        total += dict[key] if dict[key] > 0 else 0
    return total

def get_change_count_to_anagram(s):
    len_s = len(s)
    if len_s % 2 != 0:
        return -1
    s1, s2 = get_two_strings(s, len_s//2)
    target_dict = get_dict(s2)
    first_string_dict = get_dict(s1)
    for char in first_string_dict.keys():
        if target_dict.get(char):
            target_dict[char] -= first_string_dict[char]
    return sum_different_dict_values(target_dict)

import collections
def num_changes_with_arrays(s):
    if len(s) % 2 != 0:
        return -1
    else:
        string1 = s[:len(s)/2]
        string2 = s[len(s)/2:]
        c1 = collections.Counter(string1) # Oh, this is what I implemented with a dict.
        c2 = collections.Counter(string2)
        count = 0
        for letter in set(c1.keys() + c2.keys()):
            count += diff_in_letter_count(letter, c1, c2) 
        return count/2
    
def diff_in_letter_count(letter, c1, c2):
    return abs(c1[letter] - c2[letter]) #magic here, if the counter object does not contain letter as a key, returns 0

cases = int(raw_input())
for case in xrange(cases):
    s = raw_input()
    print get_change_count_to_anagram(s)

s = 'aassdfcbbs'
print get_change_count_to_anagram(s)
print num_changes_with_arrays(s)
