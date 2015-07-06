def find(l, r):
    total = 0
    for i in xrange(l-1, r):
        total = abs(total + array[i])
    return 'Even' if total % 2 == 0 else 'Odd'

n, q = [int(x) for x in raw_input().split()]
array = [int(x) for x in raw_input().split()]
for _ in xrange(q):
    l, r = [int(x) for x in raw_input().split()]
    print find(l, r)
