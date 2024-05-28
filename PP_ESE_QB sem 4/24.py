class Parent:
   def __init__(self):
       print("Parent class constructor")
   def parentMethod(self):
       print("Parent class method")
class Child(Parent):
   def __init__(self):
       super().__init__()
       print("Child class constructor")
   def childMethod(self):
       print("Child class method")
# Creating object of child class
child = Child()
child.childMethod()
child.parentMethod()