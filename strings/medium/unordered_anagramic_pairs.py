from collections import *

def get_substrings_as_anagrams_and_frequencies(s):
    check = defaultdict(int)
    len_s = len(s)
    for i in xrange(len_s):
        for j in xrange(i+1,len_s+1):
            sub = list(s[i:j])
            sub.sort()
            sub = "".join(sub)
            check[sub]+=1
    return check

def factorial(n):
    total = 1
    for i in xrange(1, n+1):
        total *= i
    return total

def combination(n, k):
    numerator = factorial(n)
    denominator = factorial(k) * factorial(n - k)
    return numerator / denominator

def count_anagramic_paris(s):
    check = get_substrings_as_anagrams_and_frequencies(s)
    total = 0
    for i in check:
        n = check[i]
        # total += (n*(n-1))/2 # matching pairs, simplified from combination equation
        total += combination(n, 2)
    return total

# cases = int(raw_input())
# for _ in xrange(cases):
#     s = raw_input()
#     print count_anagramic_paris(s)

print count_anagramic_paris('abba')
