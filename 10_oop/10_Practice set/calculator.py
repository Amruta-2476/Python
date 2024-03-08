# write a class calculator capable of finding square, cube and square root of a number
class Calculator:
    def __init__(self, num):
        self.number = num
    def square(self):
        print(f"Square of the given number is {self.number **2}")
    def cube(self):
        print(f"Cube of the given number is {self.number **3}")
    def squareRoot(self):
        print(f"Cube of the given number is {self.number **0.5}")

n = int(input("Enter a number : "))
num = Calculator(n)
num.square()
num.cube()
num.squareRoot()
    