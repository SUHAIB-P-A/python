# class definition
class Mysampleclass:
    # func definision
    def hello():  # in other python doc in class inside func contain a 'self' parameter but here what ever it is not mantatory
        print("hello")
    print("haii")


# object of the class
x = Mysampleclass
# function calling inside the class methord 1
x.hello()
# function calling inside the class methord 2
Mysampleclass.hello()
