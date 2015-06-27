#!/bin/python

def printArray(ar):
    print ' '.join([str(x) for x in ar])

def insertionSortStep(ar, end_index):    
    v = ar[end_index]
    index = end_index - 1
    
    while v < ar[index] and index >= 0:
        ar[index+1] = ar[index]
        index -=1

    ar[index+1] = v
    printArray(ar)
    return ar

def insertionSort(ar):
    len_ar = len(ar)
    for i in xrange(1, len_ar):
        ar = insertionSortStep(ar, i)

m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)
