# Enter your code here. Read input from STDIN. Print output to STDOUT
def get_is_valid(array, i, left_sum, right_sum):
    if i - 1 >= 0 and (left_sum - array[i] == right_sum):
        return True
    return False

def find_balance_index(array):
    len_array = len(array)
    if len_array < 2:
        return 'YES'
    right_sum = sum(array)
    left_sum = 0
    is_valid = False
    for i in xrange(len_array):
        left_sum += array[i]
        right_sum -= array[i]
        if left_sum > right_sum:
            is_valid = get_is_valid(array, i, left_sum, right_sum)
            break
    return 'YES' if is_valid else 'NO'


cases = int(raw_input())
for _ in xrange(cases):
    _ = raw_input()
    array = [int(x) for x in raw_input().split()]
    print find_balance_index(array)
