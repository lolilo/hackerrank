# def find(l, r):
#     total = 0
#     for i in xrange(l-1, r):
#         total = abs(total + array[i])
#     return 'Even' if total % 2 == 0 else 'Odd'
def memoize(f):
    cache = {}
    def decorated_function(*args):
        if args in cache:
            return cache[args]
        else:
            cache[args] = f(*args)
            return cache[args]
    return decorated_function

# @memoize

cache = {} # keys = l, r; values = odd or even

def calc_total_odd(l, r):
    total_odd = 0
    for i in xrange(l-1, r):
        total_odd += 1 if array[i] % 2 != 0 else 0
    return total_odd

def find(l, r):
    total_odd = calc_total_odd(l, r)
    return 'Even' if total_odd % 2 == 0 else 'Odd'

n, q = [int(x) for x in raw_input().split()]
array = [int(x) for x in raw_input().split()]
for _ in xrange(q):
    l, r = [int(x) for x in raw_input().split()]
    print find(l, r)
