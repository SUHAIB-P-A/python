# simple output
print("hello world")

# adding two numbers
a = 10
b = 20
print(a+b)

# concatination string and a number
c = a+b
print("sum of to numbers: "+str(c)+" is the sum of two no.")

# get input from user
d = input("enter a number or string")
print("user input number or string:  "+str(d))

# another methord for getting values
e = input("enter two numbers")  # here 'e' is cosidered as a string
f = input()  # here 'f ' is cosidered as a string
print(e, f)  # so there for no need for 'str()' function for printing

# convertion of input getting values 'str --> int'
sum = e+f
# here the result is 'sum = 3020' because here it is two string are added
print("sum = "+sum)

sum1 = int(e)+int(f)
# here the result is 'sum = 50' because here it is two integer are added
print("sum = "+str(sum1))


# average of three numbers
num1 = int(input('enter 3 munbers'))
num2 = int(input())
num3 = int(input())

avg = (num1+num2+num3)/3
print("average = "+str(avg))

# swaping program with two numbers
g = int(input('g val = '))
h = int(input('h val = '))

temp = g
g = h
h = temp

print("g val = "+str(g)+' h val = '+str(h))

#  function 'type'
i = 10
j = input('value')

# here type func is used to identify the type of stored value
print(type(i))  # output is '<class 'int'>'
print(type(j))  # output is '<class 'str'>'


""" string manipulating methords
    more reffer w3schools.com      
"""
k = 'hai hello my name is suhail'
print(k)  # output is "hai hello my name is suhail"
print(k[10])  # output is "m"
print(k.upper())  # output is "HAI HELLO MY NAME IS SUHAIL"
print(k[4:10])  # output is "hello"
print(k[-10:-1])  # output is "is suhai"
