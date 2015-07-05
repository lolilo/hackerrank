# Enter your code here. Read input from STDIN. Print output to STDOUT

def get_palindrome_creation_index(s):
    len_s = len(s)
    for i in xrange(len_s//2):
        comparison_char_index = len_s - 1 - i
        if s[i] == s[comparison_char_index]:
            continue
        if s[i] == s[comparison_char_index - 1]:
            if i + 1 < len_s and s[i+1] == s[comparison_char_index -2]:
                return comparison_char_index
        return i
    return -1

cases = int(raw_input())
for _ in xrange(cases):
    s = raw_input()
    print get_palindrome_creation_index(s)

print get_palindrome_creation_index('hgygsvlfwcwnswtuhmyaljkqlqjjqlqkjlaymhutwsnwcflvsgygh')
