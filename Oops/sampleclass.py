# class definition
class Mysampleclass:
    # func definision
    def hello(self, name, addr):  # in other python doc in class inside func contain a 'self' parameter but here what ever it is not mantatory
        self.names = name  # self means obj of the class that store the value in different variables
        self.names1 = 'haii hello'
        self.address = addr
        print("hello "+name)

    def print_name(self):
        # we will create a another func and it will print using self obj
        print(self.names)
        print(self.names1)
        print(self.address)
    print("haii")


# object of the class
x = Mysampleclass
# function calling inside the class methord 1
name = 'suhail'
address = """
paraalahayaur,
trssur,
keaa
"""
x.hello(x, name, address)  # parameter passing
# function calling inside the class methord 2
Mysampleclass.hello(x, name, address)
x.print_name(x)  # calling of the func
