# problem ?
"""
   *
  * *
 * * *  
"""  # code for this pattern
n = int(input('enter the no of rows'))
i = 1
while i <= n:
    j = 1
    while j <= n-i:
        print('', end=" ")
        j += 1

    j = 1
    while j <= i:
        print('*', end=" ")
        j = j+1

    print('')
    i = i+1


# problem

n = 5  # Number of rows
i = 1

while i <= n:
    # Print spaces before numbers
    j = 1
    while j <= n - i:
        print(" ", end=" ")
        j += 1

    # Print numbers in ascending order
    j = 1
    while j <= i:
        print(j, end=" ")
        j += 1

    # Print numbers in descending order (excluding 1)
    j = i - 1
    while j >= 1:
        print(j, end=" ")
        j -= 1

    print()
    i += 1


# problem ?
"""
* * * *
 * * *
  * * 
   *
"""

n = int(input('enter the no of rows'))
i = 1
while i <= n:
    j = 1
    while j <= i:
        print('', end=" ")
        j += 1

    j = n
    while j >= i:
        print('*', end=" ")
        j = j-1

    print('')
    i = i+1


# problem

"""
*
* *
* * *
* *
*
"""

n = int(input('enter the no of rows'))
# first half +1
i = 1
while i <= (n/2)+1:
    j = 1
    while j <= i:
        print('*', end=" ")
        j = j+1

    print('')
    i = i+1
# secound half
i = 1
while i <= (n/2):
    j = (n/2)
    while j >= i:
        print('*', end=" ")
        j = j-1

    print('')
    i = i+1