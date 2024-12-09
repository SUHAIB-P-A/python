#!/bin/python3

import math
import os
import random
import re
import sys


"""Sam's house has an apple tree and an orange tree that yield an abundance of fruit. Using the
information given below, determine the number of apples and oranges that land on Sam's
house.
In the diagram below:
The red region denotes the house, where s is the start point, and t is the endpoint. The
apple tree is to the left of the house, and the orange tree is to its right.
• Assume the trees are located on a single point, where the apple tree is at point a, and the
orange tree is at point b.
• When a fruit falls from its tree, it lands d units of distance from its tree of origin along the
-axis. *A negative value of d means the fruit fell d units to the tree's left, and a positive value
of d means it falls d units to the tree's right. *

Given the value of d for m apples and n oranges, determine how many apples and oranges
will fall on Sam's house (I.e., in the inclusive range [s, t])?
For example, Sam's house is between s 7 and t = IO. The apple tree is located at a 4
and the orange at b 12. There are m = 3 apples and n = 3 oranges. Apples are thrown
apples = [2, 3, —4] units distance from a, and oranges = [3, —2, —4] units distance. Adding
each apple distance to the position of the tree, they land at [4 + 2,4 + + 4]
Oranges land at [12 + 3, 12 + -2, 12 + -4]
= [15, IO, 8]. One apple and two oranges land
in the inclusive range 7 — 10 so we print

Function Description
Complete the countApplesAndOranges function in the editor below. It should print the
number of apples and oranges that land on Sam's house, each on a separate line.
countApplesAndOranges has the following parameter(s):
s: integer, starting point of Sam's house location.
t: integer, ending location of Sam's house location.
a: integer, location of the Apple tree.
b: integer, location of the Orange tree.
apples: integer array, distances at which each apple falls from the tree.
oranges: integer array, distances at which each orange falls from the tree.

"""

#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#


def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    app = 0
    orng = 0
    for apple in apples:
        positionApple = a + apple
        if positionApple >= s and positionApple <= t:
            app += 1
    for orange in oranges:
        positionOrange = b + orange
        if positionOrange >= s and positionOrange <= t:
            orng += 1

    print(app)
    print(orng)


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
