class first:
    def dispaly_first(self):
        print("first")


class secound:
    def dispaly_secound(self):
        print("secound")


class third(first, secound):  # multiple inheritence
    def dispaly_third(self):
        print("third")

x=third

x.dispaly_third(x)
x.dispaly_first(x)
x.dispaly_secound(x)