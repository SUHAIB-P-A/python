#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'rotateLeft' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER d
#  2. INTEGER_ARRAY arr
#

def rotateLeft(d, arr):
    # Write your code here
    # length = len(arr)
    # print(length)
    
    
    d = d % len(arr)
    
    # Slices methord
    arr = arr[d:]+arr[:d]
    
    return arr
    
    # def rotation(array):
    #     temp = array[0]
    #     for i in range(length-1):
    #         array[i]=array[i+1]
    #     array[length-1]=temp
    #     print(array)
    #     return array
        
    
   
    # array1 = rotation(arr)
    # i=1
    # for i in range(d-1):
    #     array2 = rotation(array1)
    
    
    # return array2
        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = rotateLeft(d, arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
