class base:
    def __init__(self):  # sinple constarctor
        print("base init")

    def set_name(self, name):
        self.name = name


class subclass(base):  # subclass inherited base a copy of base inside the subclass

    def __init__(self):  # constroctor overreading example
        print("subclass init")

    def set_name(self, name):# function overreadig
        self.name = name
        print("sub func overreading")    

    def print_welcom(self):
        print("welcom")

    def dispaly_name(self):
        print(self.name)


x = subclass()  # object creation

x.print_welcom()
x.set_name("suhail")
x.dispaly_name()
