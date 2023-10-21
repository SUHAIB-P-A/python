# example for function overloading
class sample:
    def set_name(self, name):
        self.name = name

# th is add methord is used to replace the "+" symple to this line of code "fullname=first_name+secound_name"
    def __add__(self, other):
        name = self.name+" "+other.name
        return name


first_name = sample()
secound_name = sample()

first_name.set_name("suhail")
secound_name.set_name("k k")

fullname = first_name+secound_name  # the "+" symple is replaced in "__add__()"
print(fullname)
# so this is the methord for two object add
