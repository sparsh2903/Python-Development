'''trying to make a calculator'''

class Calculator:
    def __init__(self, num):
        self.number = num

    def square(self):
        print(f"square of {self.number} is {self.number **2}")

    def squareRoot(self):
        print(f"square root of {self.number} is {self.number **0.5}")

    def cube(self):
        print(f"cube of {self.number} is {self.number **3}")
    
    @staticmethod
    def greet():
        print("here are your wishfull answers...")

a = Calculator(9)
a.greet()
a.square()
a.squareRoot() 
a.cube()