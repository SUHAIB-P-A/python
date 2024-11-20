#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    # print(s[:2])
    # print(s[3:5])
    # print(s[-4:-2])
    # print(s[-2:])
    
    hour = int(s[:2])
    formatted_hour = f"{hour:02d}"
    print(formatted_hour)
    minute, secound= s[3:5], s[-4:-2]
    
    if hour == 12 and s[-2:]=='AM':
        formatted_hour = '00'
    elif s[-2:]=='PM':
        if hour!=12:
            hour += 12
        formatted_hour = f"{hour:02d}"
        
    military_time = str(formatted_hour)+':'+str(minute)+':'+str(secound)
    # print(military_time)
    return military_time

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
