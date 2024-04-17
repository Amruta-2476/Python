class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_details(self):
        return f"Name: {self.name}, Age: {self.age}"

person_obj = Person("John", 25)

#  Print details of both class and object created.
print("Details of Class:")
print(f"Class Name: {Person.__name__}")
print(f"Class Docstring: {Person.__doc__}")
print(f"Class Variables: {Person.__dict__}")

print("\nDetails of Object:")
print(f"Object Type: {type(person_obj).__name__}")
print(f"Object Variables: {person_obj.__dict__}")
print(person_obj.display_details())


