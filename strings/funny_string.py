test_case_count = int(raw_input())

def is_funny(string, reversed_string):
    for i in xrange(1, len(string)):
        if not abs(ord(string[i]) - ord(string[i - 1])) == abs(ord(reversed_string[i]) - ord(reversed_string[i-1])):
            return False
    return True

def print_funny_judgement(test_case_count):
    for test_num in xrange(test_case_count):
        string = raw_input()
        reversed_string = string[::-1]
        print 'Funny' if is_funny(string, reversed_string) else 'Not Funny'

print_funny_judgement(test_case_count)
