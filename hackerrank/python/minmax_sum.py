#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def miniMaxSum(arr):
    # Write your code here
    result = []
    for i in range(len(arr)):
        count = 0
        temp = arr[i]
        arr[i] = 0
        for j in arr:
            count += j
        arr[i] = temp
        result.append(count)
    min_value = min(result)
    max_value = max(result)
    print(str(min_value) + " " + str(max_value))


    # optimized methord:
    total_sum = sum(arr)

    min_value = total_sum - max(arr)
    max_value = total_sum - min(arr)

    print(f"{min_value} {max_value}")


if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
