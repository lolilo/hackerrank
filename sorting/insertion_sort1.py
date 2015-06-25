#!/bin/python

def printArray(ar):
    # for element in ar:
    #     print element,
    # print
    # print ' '.join(str(x) for x in ar)
    print ' '.join([str(x) for x in ar])

# ', '.join([str(x) for x in list])  # list comprehension
# ', '.join(str(x) for x in list)    # generator expression

def insertionSort(ar):    
    v = ar[-1]
    index = len(ar) - 2
    
    while v < ar[index] and index >= 0:
        ar[index+1] = ar[index]
        printArray(ar)
        index -=1

    ar[index+1] = v
    printArray(ar)

    return ""

m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)
