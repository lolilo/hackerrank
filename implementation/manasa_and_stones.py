# Enter your code here. Read input from STDIN. Print output to STDOUT
# def find_possibilities(num, n, a, b):
#     if n < 2:
#         return [num]
#     return find_possibilities(num + a, n - 1, a, b) + find_possibilities(num + b, n - 1, a, b)


def find_possibilities(num_stones, a, b):
    set_possibilities = set()
    for num in xrange(num_stones):
        set_possibilities.add((num_stones - num - 1) * a + num * b)
    return set_possibilities


cases = int(raw_input())

for case in xrange(cases):
    num_stones = int(raw_input())
    a = int(raw_input())
    b = int(raw_input())
    set_possibilities = set(find_possibilities(num_stones, a, b))
    possibilities = [str(x) for x in sorted(list(set_possibilities))]
    print ' '.join(possibilities)
