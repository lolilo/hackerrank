# Enter your code here. Read input from STDIN. Print output to STDOUT

def get_min(array):
    min = 1000
    for num in array:
        if num != 0 and num < min:
            min = num
    return min

def print_cuts(len_array, array, sticks_gone=0):
    if sticks_gone >= len_array:
        return
    print len_array - sticks_gone
    min_num = get_min(array)
    cut_sticks = 0
    for i in xrange(len_array):
        if array[i] > 0:
            array[i] = array[i] - min_num
            if array[i] < 1:
                cut_sticks += 1
    print_cuts(len_array, array, sticks_gone + cut_sticks)
       

len_array = int(raw_input())
array = [int(x) for x in raw_input().split()]
print_cuts(len_array, array)
