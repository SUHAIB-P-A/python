import sum  # this is the example for import a file in another file
import sum as s  # in this code large module name shotern use 'as'
print(__name__)  # in this code will write any running file it will print '__main__'
# in this code write on the imported file it will print the file name like 'sum'

print(sum.__name__)  # in this code same as it will print imported file name

# the below code is function call of the 'summasion func'
sum.summasion(num1=2, num2=3)
# after import a file it will run all type code in that sum file
# example is the two print func in sum file

s.printwelcome()  # use sum -->s

# another way for call a function in imported file
result = sum.summasion  # it is a variable methord
result(20, 30)  # in the summasion func put it the result variable
# then the result variable act as a summasion func
