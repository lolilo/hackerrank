# Enter your code here. Read input from STDIN. Print output to STDOUT

def get_imba(n):
    if n % 2 != 0:
        ranks1 = range(1, (n+1)/2)
        ranks2 = range((n+1)/2, n+1)
        out = []
        # print ranks1, ranks2
        for _ in xrange((n+1)/2):
            if ranks2:
                out.append(ranks2.pop(0))
            if ranks1:
                out.append(ranks1.pop())
        return ' '.join([str(x) for x in out]) 
    ranks1 = range(1, (n+1)/2 +1)
    ranks2 = range((n+1)/2 +1, n+1)
    out = []
    # print ranks1, ranks2
    for _ in xrange((n+1)/2):
        if ranks1:
            out.append(ranks1.pop())
        if ranks2:
            out.append(ranks2.pop(0))
    return ' '.join([str(x) for x in out]) 
    

cases = int(raw_input())
for _ in xrange(cases):
    n = int(raw_input())
    print get_imba(n)

print get_imba(4)
print get_imba(7)