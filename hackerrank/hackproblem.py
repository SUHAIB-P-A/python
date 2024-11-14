#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def plusMinus(arr):
    # Write your code here
    positive = 0
    negative = 0
    zero = 0
    for num in arr:
        if num > 0:
            positive = positive+1
        elif num < 0:
            negative = negative+1
        elif num == 0:
            zero += 1
    # print(positive, negative, zero)
    length = len(arr)
    positivenum = positive/length
    negativenum = negative/length
    zeronum = zero/length
    print(f"{positivenum:.6f}\n", f"{negativenum:.6f}\n", f"{zeronum:.6f}\n")
   


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
