# in some cases we donot use the all imported file 
# we use only some func on the file
# so in that case we will write it as

from sum import summasion,printwelcome# from which module/file import which func we get all the func in the file separated using ','
from sum import printwelcome as welcome

summasion(2,3)
result=summasion
result(20,30)

printwelcome()# print 'welcome'
welcome()# print 'welcome'

# errors
#sum.summasion(2,3)# it is  an errorbecause here not use the all module
