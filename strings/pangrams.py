# Enter your code here. Read input from STDIN. Print output to STDOUT
import string

def is_panagram(s, alphabet):
    for char in s:
        char = char.lower()
        if char in alphabet:
            alphabet.remove(char)
        if len(alphabet) < 1:
            return True
    return False

def is_panagram_easy(s, alphabet): # but more expensive
    string_set = set(s.lower())
    return alphabet.issubset(string_set)
    
alphabet = set(string.ascii_lowercase)
s = raw_input()
print 'pangram ' if is_panagram_easy(s, alphabet) else 'not pangram'
