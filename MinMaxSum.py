# Input has five postive numbers
# Get minimum and maximum values that
# can be obtained by summing 4/5 ints
# print both values on two space separated output
# inputs should be between 1 and 10^9
# output (min max) sums

import math
import os
import random
import re
import sys


# Procedure
# Ensure array is ordered in ASC
# to get min sum the first n -1 elements
# to get max sum the last n -1 elements

# Use bubble sort to sort the array in ASC
def sort_array(arr):
    for i in range(0,len(arr)-1):
        for j in range(i,len(arr)):
            if arr[j] < arr[i]:
                temp = arr[j]
                arr[j] = arr[i]
                arr[i] = temp
    return arr

def miniMaxSum(arr):
    max,min = 0,0

    arr = sort_array(arr)

    for i in range(0,len(arr) - 1):
        if arr[i] >= 1 and arr[i] <= pow(10,9):
            min = min + arr[i]
    
    for j in range(1,len(arr)):
        if arr[j] >= 1 and arr[j] <= pow(10,9):
            max = max + arr[j]
    
    print(min,max)



#arr = [1,3,5,7,9]
arr = [5,9,1,7,3]
miniMaxSum(arr)

# arr = [5,9,1,7,3]
# print(sort_array(arr))
