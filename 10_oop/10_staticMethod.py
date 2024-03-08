class Employee:
    company = "Google"
    def getSalary(self):   
        print(f"Salary for {self.name} working in {self.company} is {self.salary}")

    @staticmethod
    def greet():
        print("Good morning sir")

    @staticmethod
    def time():
        print("Time is 9am")

harry = Employee()
harry.salary = 100000
harry.name = "Harry"
harry.getSalary()
harry.greet()
harry.time()
