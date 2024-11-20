#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#


def gradingStudents(grades):
    # Write your code here
    result = []
    for grade in grades:
        if grade <= 34:
            result.append(grade)
        elif grade > 34:
            nextMultipleOf5 = grade + (5 - grade % 5)
            # print(nextMultipleOf5)
            roundUp = nextMultipleOf5 - grade
            if roundUp < 3:
                result.append(nextMultipleOf5)
            else:
                result.append(grade)
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
