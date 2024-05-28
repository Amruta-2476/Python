class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display_person(self):
        print(f"Name: {self.name}\nAge: {self.age}")

class Academic:
    def __init__(self, grade):
        self.grade = grade
    def display_academic(self):
        print(f"Grade: {self.grade}")

class Sports:
    def __init__(self, sports_grade):
        self.sports_grade = sports_grade
    def display_sports(self):
        print(f"Sports Grade: {self.sports_grade}")

class Student(Person, Academic, Sports):
    def __init__(self, name, age, grade, sports_grade):
        Person.__init__(self, name, age)
        Academic.__init__(self, grade)
        Sports.__init__(self, sports_grade)
    def display_student(self):
        print(f"{self.name} is a student")


# Creating an object for the Student class
student = Student('Amruta', '20', '98', '79')
# Calling methods from each base class
student.display_person()
student.display_academic()
student.display_sports()
student.display_student()

