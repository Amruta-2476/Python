# self parameter = references the current instance of the class
# it is used to access properties and methods of that class.
class Employee:
    company = "Google"
    # def getSalary():  #TypeError: Employee.getSalary() takes 0 positional arguments but 1 was given
    def getSalary(self):   
        # print("Salary is 100K")
        print(f"Salary for {self.name} working in {self.company} is {self.salary}")
harry = Employee()
harry.salary = 100000
harry.name = "Harry"
harry.getSalary()

ginny = Employee()
ginny.salary = 999999
ginny.name = "Ginny"
ginny.getSalary()