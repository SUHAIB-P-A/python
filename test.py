n = int(input('enter the no of rows'))
i = 1
while i <= (n/2)+1:
    j = 1
    while j <= n-i:
        print('', end=" ")
        j += 1

    j = 1
    while j <= i:
        print('*', end="")
        j = j+1

    print('')
    i = i+1
i=1    
while i <= (n/2):
    j = (n/2)
    while j >= i:
        print('', end=" ")
        j -= 1

    j = (n/2)
    while j >= i:
        print('*', end="")
        j = j-1

    print('')
    i = i+1    