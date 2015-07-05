# Enter your code here. Read input from STDIN. Print output to STDOUT

def get_new_char_ord(char, k, starting_ord, ending_ord):
    new_ord = ord(char) + k
    while new_ord > ending_ord:
        new_ord -= 26
    while new_ord < starting_ord:
        new_ord += 26
    return new_ord
    
def get_cipher(s, k):
    ciphered_string = ''
    ord_a = ord('a')
    ord_z = ord('z')
    ord_A = ord('A')
    ord_Z = ord('Z')

    for char in s:
        if ord_a <= ord(char) <= ord_z:
            new_char_ord = get_new_char_ord(char, k, ord_a, ord_z)
            ciphered_string += chr(new_char_ord)
        elif ord_A <= ord(char) <= ord_Z:
            new_char_ord = get_new_char_ord(char, k, ord_A, ord_Z)
            ciphered_string += chr(new_char_ord)
        else:
            ciphered_string += char

    return ciphered_string

_ = raw_input()
s = raw_input()
k = int(raw_input())
print get_cipher(s, k)
