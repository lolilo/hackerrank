# Enter your code here. Read input from STDIN. Print output to STDOUT

def count_numbers(array):
    count_array = [0] * 100 # 0 to 99 inclusive
    for num in array:
        count_array[num] += 1
    return count_array

def print_count_arary(count_array):
    for num in xrange(len(count_array)):
        for i in xrange(count_array[num]):
            print num,
            
def counting_sort(array):
    count_array = count_numbers(array)
    print_count_arary(count_array)

_ = raw_input()
array = [int(x) for x in raw_input().split()]
counting_sort(array)
