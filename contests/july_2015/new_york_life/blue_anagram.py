# Complete the function below.

def make_dict(str):
    d = {}
    for char in str:
        if d.get(char):
            d[char] += 1
        else:
            d[char] = 1
    return d

def is_anagram(word1, word2):
    d1 = make_dict(word1)
    d2 = make_dict(word2)
    for key in d2.keys():
        if not d1.get(key) or d1[key] != d2[key]:
            return False
    return True

def make_x(word):
    return 'X' * len(word)
    
def replaceBLUE(str):
    new_str = ''
    words = str.split()
    for word in words:
        if is_anagram('BLUE', word):
            new_str += make_x(word)
        else:
            new_str += word
        new_str += ' '
    return new_str
        
