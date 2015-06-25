# Enter your code here. Read input from STDIN. Print output to STDOUT
# target_int = int(raw_input())
# len_array = int(raw_input())
# array = [int(x) for x in raw_input().split()]

def binary_search_shitty(array, target):
    start = 0
    end = len(array)
    curr_index = end // 2
    
    while start <= end:
        print start, end, curr_index
        if target < array[curr_index]:
            end = curr_index - 1
            curr_index = curr_index - (curr_index - start) // 2
        elif target > array[curr_index]:
            start = curr_index + 1
            curr_index = curr_index + (end - curr_index) // 2
        else:
            return curr_index
    return None

# print binary_search_shitty(array, target_int)
print binary_search_shitty(range(10), 11)
