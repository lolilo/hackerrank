def find_largest_three_factorial(n):
    return n - (n % 3)

def get_num(n):
    fives = find_largest_three_factorial(n)
    fives_possible = True if fives > 0 else False
    if fives_possible:
        while (n - fives) % 5 != 0:
            fives -= 3
            if fives < 3:
                fives_possible = False
                break
    if fives_possible:
        threes = n - fives
    else:
        fives = 0
        threes = n if n % 5 == 0 else -1
    return '5' * fives + '3' * threes if fives >=0 and threes >= 0 else -1

cases = int(raw_input())
for _ in xrange(cases):
    n = int(raw_input())
    print get_num(n)
