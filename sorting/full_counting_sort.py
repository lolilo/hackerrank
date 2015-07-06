# Enter your code here. Read input from STDIN. Print output to STDOUT

def parse_list(size):
    count_array = [0] * 100 # 0 to 99
    for i in xrange(size):
        num, _ = [x for x in raw_input().split()]
        num = int(num)
        count_array[num] += 1
    for i in xrange(1, 100):
        count_array[i] += count_array[i-1]
    print ' '.join([str(x) for x in count_array])

size = int(raw_input())
parse_list(size)
