# Enter your code here. Read input from STDIN. Print output to STDOUT

def partition1(array, start, end):
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
      return i

def partition2(array, start, end): # Lomuto Partitioning method
      pivot = array[end]
      store_index = start
      for i in xrange(start, end):
        if array[i] < pivot:
          array[i], array[store_index] = array[store_index], array[i] 
          # store_index will always be >= current value
          store_index += 1
      array[store_index], array[end] = pivot, array[store_index]
      return store_index

def quick_sort(array, start, end):
      if start < end:
        split_point = partition2(array, start, end)
        print ' '.join(map(str, array))
        quick_sort(array, start, split_point-1)
        quick_sort(array, split_point+1, end)
    
not_used = raw_input()
array = [int(x) for x in raw_input().split()]
# array = '1 3 9 8 2 7 5'
# array = '1 3 1 1 1'
# array = '3 1'
# array = '9 8 6 7 3 5 4 1 2'
# array = [int(x) for x in array.split()]
quick_sort(array, 0, len(array) - 1)
