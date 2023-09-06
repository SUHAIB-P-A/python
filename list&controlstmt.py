# in this code no problem
name = "suhail baas"
print(name[5])

# but, suppose we will change a letter in that string! like this
# name[5]='f'# in this code show error "TypeError: 'str' object does not support item assignment" because string is immutable
print(name[5])

# list concept in python
list_items = ['suhail', 'sugu', 'ubu']
print(list_items)  # output is "['suhail', 'sugu', 'ubu']"
print(list_items[0])  # output is "suhail"
print(list_items[0:1])  # output is "['suhail']"
print(list_items[0:])  # output is "['suhail', 'sugu', 'ubu']"
print(list_items[-1])  # output is "ubu"
print(list_items[-3:])  # output is "['suhail', 'sugu', 'ubu']"
print(list_items[:-1])  # output is "['suhail', 'sugu']"
print(list_items[-3:-2])  # output is "['suhail']"
# MORE ABOUT LIST CHECK W3SCHOOL.COM

# add another list  inside a  existing list
list_items = list_items+["apple", 'orange', 'water malon', 10]
# output is "['suhail', 'sugu', 'ubu', 'apple', 'orange', 'water malon',10]"
print(list_items)

# add value in the list 'list_items' at the last position using append() func
list_items.append('Avocado')
# output is "['suhail', 'sugu', 'ubu', 'apple', 'orange', 'water malon', 10, 'Avocado']"
print(list_items)

# user inputing a value from a list last pisition
#list_items.append(input("enter a value"))
# output is "['suhail', 'sugu', 'ubu', 'apple', 'orange', 'water malon', 10, 'Avocado', 'Blueberry']"
print(list_items)
# here blueberry is user inputed

# insert func in list
list_items.insert(2, "Black currant")
# output is "['suhail', 'sugu', 'Black currant', 'ubu', 'apple', 'orange', 'water malon', 10, 'Avocado']"
print(list_items)
# here 'Black currant' is added at the 2ed position of the list

# user inputting methord for insert
# a error the positon is int input func take string so we will convert int
#list_items.insert(int(input('enter the position')), input('enter a value'))
# output is "['suhail', 'mango', 'sugu', 'Black currant', 'ubu', 'apple', 'orange', 'water malon', 10, 'Avocado']"
print(list_items)


# control statement.........
# here if entered value is 0 the output is +ve
# num = int(input('enter a number'))
# if num < 0:  # so in this situvation we will use 'elif'
#     print('number is -ve')
# elif num == 0:
#     # !!! FORMAT ARE MUST BE FOLLOW IN CONTROL STATEMENT !!!
#     print('number is zero')
# else:
#     print('number is +ve')


# loops...........
# 1.while loop
i = 1
while i <= 10:
    print(i)     # here while loop can provide else codisions
    i = i+1
# here the example for else
else:
    print("loop finished")

# 2.forloop
files = ['Iratta.mp4', 'Ntikkakkakkoru Premandaarnnu.mp4', 'Thankam.mp4']
for x in files:
    print(x)
    print(x[0:-4])   # here 0 indicate starting of the string and -4 indicate
    # after '.' posion

# in numbers for loop we use range function
for i in range(1, 11, 2):  # here three parameter 'start','stop','step/divide'
    print(i)





# problem ?
# multiplication table code
# ans = 0
# m = int(input('enter a number your multipication'))
# rng=int(input('enter the range of multipication'))
# for n in range(1, rng+1):
#     ans = n*m
#     print(str(m)+' * '+str(n)+' = '+str(ans))


# problem ?
"""
   *
  * *
 * * *  
"""  # code for this pattern
n=int(input('enter the no of rows'))
i=1
while i<=n:
    j=1
    while j<=n-i:
       print('',end=" ")
       j+=1

    j=1
    while j<=i:
      print('*',end=" ")
      j=j+1

    print('')
    i=i+1
    