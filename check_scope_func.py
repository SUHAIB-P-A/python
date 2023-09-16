# in this code define local and globel scope of a function
# here we will see a func check_scope in side the func we will define three other func
def check_scope():
    def do_local():
        test = 'local test'
        print(test)

    def do_non_local():
        test = 'non loacal test'

    def do_globel():
        test = 'globel test'

    test = 'default'
    do_local()
    print('after calling do_local is: '+test)
# output is 'after calling do_local is: default'


check_scope()  # first call func --> call do_local func --> test value is 'local test' --> after executing the code test value will replaced 'default'--> after printing default the execution end
