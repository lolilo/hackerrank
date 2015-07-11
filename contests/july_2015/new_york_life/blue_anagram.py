# Complete the function below.

def make_dict(str):
    d = {}
    for char in str:
        if d.get(char):
            d[char] += 1
        else:
            d[char] = 1
    return d

def is_anagram(word):
    d1 = {'E': 1, 'B': 1, 'U': 1, 'L': 1}
    d2 = make_dict(word)
    for key in d2.keys():
        if not d1.get(key) or d1[key] != d2[key]:
            return False
    return True

def replace_anagram_with_x(start_index, str, str_len):
    word = ''
    index = start_index
    while index < str_len and str[index] != ' ':
        word += str[index]
        index += 1
    if is_anagram(word):
        make_x(start_index, index, str)
    return str, index

def make_x(start_index, end_index, str):
    index = start_index
    while index < end_index:
        str[index] = 'X'
        index += 1
    return str
    
def replaceBLUE(str):
    str = list(str)
    str_len = len(str)
    char_index = 0
    while char_index < str_len:
        char = str[char_index]
        if char == ' ':
            char_index += 1
            continue
        str, end_index = replace_anagram_with_x(char_index, str, str_len)
        char_index = end_index
    return ''.join(str)

str = '   GET    BLUEYO RID OF BLUE AND UEBL BUT LEBUS ARE GOOD    '
str = ' BL     '
print replaceBLUE(str)
print len(replaceBLUE(str))


