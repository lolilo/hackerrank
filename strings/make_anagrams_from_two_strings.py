def get_dict(s):
    d = {}
    for char in s:
        if d.get(char):
            d[char] += 1
        else: 
            d[char] = 1
    return d

def get_min_deletions_to_anagrams(s1, s2):
    deletion_count = 0
    anagram_set = set(s1).intersection(set(s2))
    d1, d2 = get_dict(s1), get_dict(s2)

    for char in d1.keys():
        if char not in anagram_set:
            deletion_count += d1[char]
        else:
            deletion_count += abs(d1[char] - d2[char])
    for char in d2.keys():
        if char not in anagram_set:
            deletion_count += d2[char]
    return deletion_count

s1 = raw_input()
s2 = raw_input()
# s1 = 'bacdc'
# s2 = 'dcbad'
# s1 = 'cde'
# s2 = 'abc'
print get_min_deletions_to_anagrams(s1, s2)