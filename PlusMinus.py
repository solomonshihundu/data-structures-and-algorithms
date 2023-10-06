#!/bin/python3

import math
import os
import random
import re
import sys

# Loop through array
# count the number of element that are:
# greater than zero
# less than zero 
# equal to zero
# divide each of the results by the total number of elements in the array
# print the result of the divide operation
def plusMinus(arr):
    
    # Get the size of the array
    arr_size = len(arr)

    #Variables to store the number of elements repectively
    pos,neg,zero = 0,0,0

    for num in arr:
        if num >= -100 and num <= 100:
            if num > 0:
                pos = pos + 1
            elif num < 0:
                neg = neg + 1
            else:
                zero = zero + 1
    
    if arr_size > 0 and arr_size <= 100:
        print_divide(pos,neg,zero,arr_size)

def print_divide(pos,neg,zero,size):
    # f'{my_float:.3f}'
    # print(round((pos/size),6),'\n')
    # print(round((neg/size),6),'\n')
    # print(round((zero/size),6),'\n')
    print(f'{pos/size:.6f}')
    print(f'{neg/size:.6f}')
    print(f'{zero/size:.6f}')
   

if __name__ == '__main__':
    # Taking intup from std in
    # n = int(input().strip())
    # arr = list(map(int, input().rstrip().split()))

    arr = [-4, 3, -9, 0, 4, 1]
    plusMinus(arr)
