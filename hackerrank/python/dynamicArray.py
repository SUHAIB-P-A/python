#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#


def dynamicArray(n, queries):
    # Write your code here
    arr = [[] for _ in range(n)]
    lastanswer = 0
    result = []

    for item in queries:
        queryType, x, y = item
        if queryType == 1:
            index = (x ^ lastanswer) % n
            arr[index].append(y)
        elif queryType == 2:
            index1 = (x ^ lastanswer) % n
            position = y % len(arr[index1])
            lastanswer = arr[index1][position]
            result.append(lastanswer)

    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
