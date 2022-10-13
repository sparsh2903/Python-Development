

# uses of self and other functions 

class Programmer:
    company = "Google"

    def __init__(self, name, product):
        self.name = name
        self.product = product

    def getInfo(self):
        print(f"The name of the comapny is {self.company} and programmer person is {self.name} of the product {self.product}")


sparsh = Programmer("sparsh", "Skype")
mayank = Programmer("mayank", "GitHub")
sparsh.getInfo()
mayank.getInfo()
