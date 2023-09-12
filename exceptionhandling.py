# it is a simple block of code for exception handling
b=10
try:# in the block we will add working code 
   a=10/b
   print(a)
except ZeroDivisionError:# in this block we will print  error massage
   print("can't divided by zero")

print("program completed")
# here the above example  no exception occur

# here is the exception handling example  
b=0
try:# in this block are not work 
   a=10/b
   print(a)
except ZeroDivisionError:# this will work because here a exception "ZeroDivisionError" 
   print("can't divided by zero")

print("program completed")


