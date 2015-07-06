# Enter your code here. Read input from STDIN. Print output to STDOUT

def partition(array, start, end): # Lomuto Partitioning method
      pivot = array[end]
      store_index = start
      step_count = 0
      for i in xrange(start, end):
        if array[i] < pivot:
          array[i], array[store_index] = array[store_index], array[i] 
          step_count += 1
          # store_index will always be >= current value
          store_index += 1
      array[store_index], array[end] = pivot, array[store_index]
      return store_index, step_count+1

def quick_sort(array, start, end):
      step_count = 0
      if start < end:
        split_point, next_step_count = partition(array, start, end)
        step_count += next_step_count
        step_count += quick_sort(array, start, split_point-1)
        step_count += quick_sort(array, split_point+1, end)
      return step_count

def insertion_sort(l):
    step_count = 0
    for i in xrange(1, len(l)):
        j = i-1 
        key = l[i]
        while (j >= 0) and (l[j] > key):
           l[j+1] = l[j]
           step_count += 1
           j -= 1
        l[j+1] = key
    return step_count

_ = raw_input()
array = [int(x) for x in raw_input().split()]

quick_steps = quick_sort(array[::], 0, len(array) - 1)
insertion_steps = insertion_sort(array[::])
print insertion_steps - quick_steps
