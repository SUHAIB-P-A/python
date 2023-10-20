class base:
    def set_name(self, name):
        self.name = name


class subclass(base):  # subclass inherited base a copy of base inside the subclass
    def print_welcom():
        print("welcom")

    def dispaly_name(self):
        print(self.name)


x = subclass  # object creation

x.print_welcom()
x.set_name(x, "suhail")
x.dispaly_name(x)
