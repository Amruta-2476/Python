# normal way => procedural programming
# a = 12
# b = 34
# print("The sum of a and b is",a+b)

# object oriented programming (OOP)
class Number:
    def sum(self):
        return self.a + self.b
num = Number()  #instance of object
num.a = 12
num.b = 34
print(num.sum())