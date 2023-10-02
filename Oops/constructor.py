class teamfootball:
    year = 2013

    def __init__(self, name, number, club):
        self.name = name
        self.number = number
        self.club = club

    def changenum(self):
        self.number = self.number+1

    def changeclub(self, club):
        self.club = club

    def display(self):
        print("name: "+self.name)
        print("age: "+str(self.number))
        print("club: "+self.club)
        print("year: "+str(teamfootball.year))

    @classmethod  # class methord for common variables in class
    def add_year(cls):
        cls.year = cls.year+1

    @staticmethod
    def display_welcome():
        print("WELCOME")


teamfootball.display_welcome()
x = teamfootball('Neymar', 11, 'Al Hilal')
y = teamfootball('Ronaldo', 7, 'Al Nasar')
x.display()
y.display()

teamfootball.year = teamfootball.year+10


print("--------------------------------------------")

teamfootball.display_welcome()
x.changenum()
x.display()

print("***********************************")

teamfootball.display_welcome()
y.changenum()
y.display()

print("--------------------------------------------")

teamfootball.display_welcome()
x.changeclub("psg")
x.display()

print("***********************************")

teamfootball.display_welcome()
y.changeclub("Real Matrid")
teamfootball.add_year()
y.display()
