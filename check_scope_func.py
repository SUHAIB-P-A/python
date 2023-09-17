# in this code define local and globel scope of a function
# here we will see a func check_scope in side the func we will define three other func
def check_scope():
    def do_local():
        test = 'local test'
        print(test)

    def do_non_local():
        nonlocal test  # keyword 'nonlocal'
        print(test)  # output is 'default'
        test = 'non loacal test'

    def do_globel():
        global test  # keyword 'globel'
        test = 'globel test'

    test = 'default'
    do_local()
    print('after calling do_local is: '+test)
    # output is 'after calling do_local is: default'

    do_non_local()  # in this case nonlocal keyword check_scope define test variable pass to the do_non_local func then it is change the test variable value 'default'-->'non loacal test' proof is do_non_local variable print
    # that test variable is print it
    print('after calling do_non_local is: '+test)
    # output is 'after calling do_non_local is: non loacal test'

    do_globel()
    print('after calling do_non_local is: '+test)
    # output is 'after calling do_non_local is: non loacal test'
    # here is print 'non loacal test' because globel keyword used variable only acess outside of the main
    # example is 'print("after check_scope is: "+test)' this code


check_scope()  # first call func --> call do_local func --> test value is 'local test' --> after executing the code test value will replaced 'default'--> after printing default the execution end
print("after check_scope is: "+test)  # globel test accesing
# output is 'after check_scope is: globel test'
