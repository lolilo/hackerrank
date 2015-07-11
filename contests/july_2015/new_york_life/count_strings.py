# Complete the function below.
import string
import itertools

def get_permutations(alphabet):
    return itertools.permutations(alphabet)

def  countStrings(l,  v):
    alphabet = set(string.ascii_lowercase)
    # for letter in alphabet:
    permutations = get_permutations(alphabet)
    for perm in permutations:
        print perm



countStrings(3, 3)

# for a in itertools.permutations([1, 1, 2]):
#     print a