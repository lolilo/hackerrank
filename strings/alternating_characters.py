# Enter your code here. Read input from STDIN. Print output to STDOUT

def count_deletions(s):
    prev_char = s[0]
    i = 1
    deletion_count = 0
    len_s = len(s)
    while i < len_s:
        while i < len_s and s[i] == prev_char:
            deletion_count += 1
            i += 1
        if i < len_s:
            prev_char = s[i]
            i += 1
    return deletion_count

def count_deletions_better(s):
    deletion_count = 0
    for i in xrange(1, len(s)):
        prev_char = s[i-1]
        current_char = s[i]
        if prev_char == current_char:
            deletion_count += 1
    return deletion_count


cases = int(raw_input())
for i in xrange(cases):
    s = raw_input()
    print count_deletions_better(s)
