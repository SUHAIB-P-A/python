# in this code no problem
name= "suhail baas"
print(name[5])

#but, suppose we will change a letter in that string! like this
#name[5]='f'# in this code show error "TypeError: 'str' object does not support item assignment" because string is immutable 
print(name[5])

# list concept in python 
list_items=['suhail','sugu','ubu']
print(list_items)# output is "['suhail', 'sugu', 'ubu']"
print(list_items[0])# output is "suhail"
print(list_items[0:1])# output is "['suhail']"
print(list_items[0:])# output is "['suhail', 'sugu', 'ubu']"
print(list_items[-1])# output is "ubu"
print(list_items[-3:])# output is "['suhail', 'sugu', 'ubu']"
print(list_items[:-1])# output is "['suhail', 'sugu']"
print(list_items[-3:-2])# output is "['suhail']"
# MORE ABOUT LIST CHECK W3SCHOOL.COM

# add another list  inside a  existing list
list_items=list_items+["apple",'orange','water malon',10]
print(list_items)# output is "['suhail', 'sugu', 'ubu', 'apple', 'orange', 'water malon',10]"

# add value in the list 'list_items' at the last position using append() func
list_items.append('Avocado')
print(list_items)# output is "['suhail', 'sugu', 'ubu', 'apple', 'orange', 'water malon', 10, 'Avocado']"

# user inputing a value from a list last pisition
list_items.append(input("enter a value"))
print(list_items)# output is "['suhail', 'sugu', 'ubu', 'apple', 'orange', 'water malon', 10, 'Avocado', 'Blueberry']"
# here blueberry is user inputed

# insert func in list
list_items.insert(2,"Black currant")
print(list_items)# output is "['suhail', 'sugu', 'Black currant', 'ubu', 'apple', 'orange', 'water malon', 10, 'Avocado']"
# here 'Black currant' is added at the 2ed position of the list

# user inputting methord for insert
list_items.insert(int(input('enter the position')),input('enter a value'))# a error the positon is int input func take string so we will convert int
print(list_items)# output is "['suhail', 'mango', 'sugu', 'Black currant', 'ubu', 'apple', 'orange', 'water malon', 10, 'Avocado']"