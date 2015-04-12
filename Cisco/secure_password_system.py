# Enter your code here. Read input from STDIN. Print output to STDOUT

from math import factorial

VALID_CHARACTERS = 10

def get_password_permutations(password_length):
    
    def permutation_with_repetition(n, r):
        return n**r

    return permutation_with_repetition(VALID_CHARACTERS, password_length)

def is_secure(total_valid_passwords): 
    return total_valid_passwords > 10**6

amount_of_test_cases = int(raw_input())

for i in xrange(amount_of_test_cases):
    min_password_length, max_password_length = [ int(x) for x in raw_input().split() ] 
    
    total_valid_passwords = 0
    for password_length in xrange(min_password_length, max_password_length + 1):
        total_valid_passwords += get_password_permutations(password_length)

    if is_secure(total_valid_passwords):
        print 'YES'
    else: 
        print 'NO'
