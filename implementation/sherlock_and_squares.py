# Enter your code here. Read input from STDIN. Print output to STDOUT
import math 

def is_square(x):
    sqroot = math.sqrt(x)
    return int(sqroot) == sqroot 

def get_squares_between(first_num, second_num):
    curr_first_num = first_num
    curr_second_num = second_num
    first_sq = -1
    second_sq = -1
    while curr_first_num <= second_num:
        if is_square(curr_first_num):
            first_sq = curr_first_num
            break
        curr_first_num += 1
    while curr_second_num >= curr_first_num:
        if is_square(curr_second_num):
            second_sq = curr_second_num
            break
        curr_second_num -= 1
    if first_sq < 0 and second_sq < 0:
        return 0
    return int(math.sqrt(second_sq) - math.sqrt(first_sq) + 1)
    

# cases = int(raw_input())
# for _ in xrange(cases):
#     first_num, second_num = [int(x) for x in raw_input().split()]
#     print get_squares_between(first_num, second_num)

