# 2 types of attributes: class attribute and instance attribute
class Employee:
    company = "Google"   #specific to the whole class and same for all objects
john = Employee()
ana = Employee()
print(john.company)
print(ana.company)
print(Employee.company)
Employee.company = "Microsoft"
print(john.company)
print(ana.company)
print(Employee.company)

# instance attributes
# class Employees:
#     def printData(self):
#         print(f"Name of employee is {self.name}")
#         print(f"Salary of employee is {self.salary}")
harry = Employee()
ginny = Employee()
harry.name = "Harry"
harry.salary = "30K"
ginny.name = "Ginny"
ginny.salary = "45K"
print(harry.name)
print(ginny.name)