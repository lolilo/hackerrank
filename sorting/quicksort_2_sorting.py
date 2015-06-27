#!/bin/python

def quickSort(ar):
    if len(ar) < 2:
        return ar
    pivot = ar[0]
    lesser_elements = []
    greater_elements = []
    for i in xrange(1, len(ar)):
        element = ar[i]
        lesser_elements.append(element) if element <= pivot else greater_elements.append(element)
    
    sorted_array = quickSort(lesser_elements) + [pivot] + quickSort(greater_elements)
    print ' '.join(map(str,sorted_array))
    return sorted_array

m = input()
ar = [int(i) for i in raw_input().strip().split()]
quickSort(ar)
