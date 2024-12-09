#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#


def nonDivisibleSubset(k, s):
    # Write your code here

    remainder_freq = [0] * k

    for number in s:
        remainder_freq[number % k] += 1
        print(remainder_freq)

    subset_size = min(remainder_freq[0], 1)

    for i in range(1, (k // 2) + 1):
        if i == k-i:
            subset_size += min(remainder_freq[i], 1)
        else:
            subset_size += max(remainder_freq[i], remainder_freq[k-i])

    return subset_size


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    fptr.write(str(result) + '\n')

    fptr.close()
