class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
    print("this is a person")

p1 = Person("John", 36)
p1.age = 40
print(p1.name)
print(p1.age)