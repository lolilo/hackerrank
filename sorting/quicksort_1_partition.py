#!/bin/python
def partition(ar):
    pivot = ar[0]
    lesser_elements = []
    greater_elements = []
    for i in xrange(1, len(ar)):
        element = ar[i]
        lesser_elements.append(element) if element <= pivot else greater_elements.append(element)
    return lesser_elements + [pivot] + greater_elements

m = input()
ar = [int(i) for i in raw_input().strip().split()]
sorted_array = partition(ar)
print ' '.join(map(str, sorted_array))
