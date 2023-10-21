class first:
    def dispaly_first(self):
        print("first")


class secound(first): # example multilevel inhertance
    def dispaly_secound(self):
        print("secound")


class third(secound):  # multiple inheritence
    def dispaly_third(self):
        print("third")

x=third()

x.dispaly_third()
x.dispaly_first()
x.dispaly_secound()