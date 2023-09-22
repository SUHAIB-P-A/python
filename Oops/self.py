class persion:
    def func1(self,name):
        self.name=name

    def func_display(self):
        print(self.name)    




# different obj use same func in the class with different variables
x=persion
y=persion
z=persion
name='suhail'
x.func1(x,name)
x.func_display(x)

y.func1(y,'ubaid')
y.func_display(y)

z.func1(z,name='suhaib')
z.func_display(z)
