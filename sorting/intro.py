# Enter your code here. Read input from STDIN. Print output to STDOUT
target_int = int(raw_input())
len_array = int(raw_input())
array = [int(x) for x in raw_input().split()]

def binary_search(array, target):
    start = 0
    end = len(array)
    while start <= end:
        curr_index = start + (end - start) // 2
        if target < array[curr_index]:
            end = curr_index - 1
        elif target > array[curr_index]:
            start = curr_index + 1
        else:
            return curr_index
    return None

print binary_search(array, target_int)

