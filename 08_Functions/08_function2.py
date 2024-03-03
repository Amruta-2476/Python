# WAP to greet a user with "Good day" using functions
def greeting(name):
    print("Good day",name)
username = input("Enter your name: ")
greeting(username)

# send a List as an argument
def my_function(food):
  for x in food:
    print(x)
fruits = ["apple", "banana", "cherry"]
my_function(fruits)