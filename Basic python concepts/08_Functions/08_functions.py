def my_function():
  print("Hello from a function")
my_function()

def myFunction(fname):  #fname=parameters
  print(fname + " Potter")
myFunction("Lily")
myFunction("Harry")  #args = Lily, Harry, James
myFunction("James")

def my_func(child3, child2, child1):
  print("The youngest child is " + child3)
my_func(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

# use a default parameter value
def funcNew(country = "Norway"):
  print("I am from " + country)
funcNew("Sweden")
funcNew("India")
funcNew()

