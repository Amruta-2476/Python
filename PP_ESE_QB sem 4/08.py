# Find the output of the following program
class data:
    def __init__(self, name):
        self.name = name
    def display(self):
        print("Hello, my name is", self.name)

t = data("Om")
t.display()