# 1) Create a class programmer for storing info of a few programmers working at microsoft
class Programmers:
    company = "Microsoft"
    def __init__(self, name, age, salary, department):
        self.name = name
        self.age = age
        self.salary = salary
        self.department = department

    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}, Department: {self.department}"

# Displaying the company
print(f"Company: {Programmers.company}")

# Creating instances using class methods
p1 = Programmers("John Doe", 30, 50000, "Software Engineering")
p2 = Programmers("Susan Storm", 28, 48000, "Marketing")

# Displaying information using the display_info method
print(p1.display_info())
print(p2.display_info())