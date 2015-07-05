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
    
alphabet = set(string.ascii_lowercase)
s = raw_input()
print 'pangram ' if is_panagram(s, alphabet) else 'not pangram'
