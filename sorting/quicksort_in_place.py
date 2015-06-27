# Enter your code here. Read input from STDIN. Print output to STDOUT
def quick_sort(array, start, end):
    if start < end:
        pivot = array[end]
        i = start
        j = end - 1
        
        done = False
        while not done:
            while array[i] <= pivot and i <= j: # find an element greater than pivot
                i += 1 
            while array[j] >= pivot and j >= i: # find an element less than pivot
                j -= 1
                
            if i > j:
                done = True
            else:
                array[i], array[j] = array[j], array[i] # swap the elements
            
        array[end], array[i] = array[i], array[end] # i will be pointing to the larger number. might be pointing to pivot itself
        print ' '.join(map(str, array))
        quick_sort(array, start, i-1)
        quick_sort(array, i+1, end)
    
# not_used = raw_input()
# array = [int(x) for x in raw_input().split()]
# array = '1 3 9 8 2 7 5'
# array = '1 3 1 1 1'
# array = '3 1'
array = [int(x) for x in array.split()]
quick_sort(array, 0, len(array) - 1)
