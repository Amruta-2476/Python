# Write a program to implement all types of inheritance in classes explaining the step-by-step execution.
# 1. Single Inheritance
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass  # Placeholder for speak method

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

dog = Dog("Buddy")
print(dog.speak())  # Output: Buddy says Woof!


# 2. Multiple Inheritance
class Flyable:
    def fly(self):
        return "I can fly!"

class Bird(Animal, Flyable):
    pass

bird = Bird("Sparrow")
print(bird.speak())  # Output: Sparrow says Woof!
print(bird.fly())    # Output: I can fly!


# 3. Multilevel Inheritance
class Puppy(Dog):
    def play(self):
        return f"{self.name} is playing!"

puppy = Puppy("Rocky")
print(puppy.speak())  # Output: Rocky says Woof!
print(puppy.play())   # Output: Rocky is playing!


# 4. Hierarchical Inheritance
class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

class Lion(Animal):
    def speak(self):
        return f"{self.name} roars loudly!"

cat = Cat("Tom")
lion = Lion("Simba")
print(cat.speak())   # Output: Tom says Meow!
print(lion.speak())  # Output: Simba roars loudly!



    

