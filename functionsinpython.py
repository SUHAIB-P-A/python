# function in python
# function defnition
def hey():
  print("helo")

# function call
hey()

# argument passing inn a function
def hello(name,age):
  print("my name is ",name,'age:'+str(age))

# hello func call
value='suhail'
hello(value,25)

# tuples
tp=('hello',"haii","whatsapp...")
print(tp[0])
"""
this is tuple it is similar to list but tuple are not allowed to modified 
values tuple can only be permit to view the values
"""

# arbitrary argument
def hello1(*values):
  print("first: "+values[0]+" secound: "+values[1],values[2])

hello1("haii","hello","how are you")  