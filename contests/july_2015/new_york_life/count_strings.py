# Complete the function below.
import string
import itertools

def factorial(n):
    factorial = 1
    for n in xrange(1, n+1):
        factorial *= n
    return factorial

def nPr(n, r):
    numerator = factorial(n)
    denominator = factorial(n-r)
    return numerator/denominator

def findsubsets(alphabet, n):
    return itertools.combinations(alphabet, n)

def get_subset_value(alphabet_value_array, subset):
    value = 0
    for char in subset:
        char_position = ord(char) - 96
        value += alphabet_value_array[char_position]
    return value

def countStrings(l, v):
    alphabet_value_array = [0] + [x**2 for x in xrange(1, 27)]
    alphabet = set(string.ascii_lowercase)
    alphabet_array = []
    for letter in alphabet:
        alphabet_array.extend([letter] * l)
    subsets = findsubsets(alphabet_array, l)
    count = 0
    count_increment = nPr(l, l)
    valid_subsets = set()
    for subset in subsets:
        subset_value = get_subset_value(alphabet_value_array, subset)
        if subset_value == v:
            if subset in valid_subsets:
                continue
            count += count_increment
            valid_subsets.add(subset)
    return count


count = countStrings(2, 13)
print count