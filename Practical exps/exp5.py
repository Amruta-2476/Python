class Person:
    def __init__(self,id, name, age, grade):
        self.id = id
        self.name = name
        self.age = age
        self.grade = grade

    def display(self):
        print(f"ID : {self.id}\nName: {self.name}\nAge: {self.age}\nGrade: {self.grade}")

class Sports(Person):
    def __init__(self,id, name, age, grade, sports_grade):
        super().__init__(id, name, age, grade)
        self.sports_grade = sports_grade

    def get_details(self):
      super().display()
      print(f"Sports Grade: {self.sports_grade}")

obj1 = Sports('22AD1015', 'Amruta', '20', '98', '79')
obj1.get_details()
print()
obj2 = Sports('22AD1016', 'John', '19', '90', '99')
obj2.get_details()
print()
obj2 = Sports('22AD1017', 'Anna', '20', '88', '89')
obj2.get_details()




