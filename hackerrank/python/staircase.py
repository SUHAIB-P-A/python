#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    # Write your code here
    for current_row in range(1, n+1):
        space = " " * (n - current_row)
        hashes = "#" * current_row
        print(space + hashes)
    

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
