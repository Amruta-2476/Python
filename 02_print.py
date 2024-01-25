# can write python hello.py in terminal to run too
name = input("What's your name? ")

# 1) 
print("Hello", name, "Welcome to python")
# OR

# 2)
print("Hello "+ name + " 14" + " years old") #concatenation using + operator
# OR

# 3)
print(f"Hello {name} using fromat string")
#USING FORMAT STRING/ F STRING

# (function) def print(
#     *values: object,
#     sep: str | None = " ",
#     end: str | None = "\n",
# ) 
# sep:- string inserted between values, default a space. So that's why when we passed 2 arguments like this ("Hello", name) we automatically get a space between the two.
# end:- string appended after the last value, default a newline. so that's why print automatically goes to a newline.

print("")
# to override these default values of the parameters:
print("Hello") 
print(name)
print("Hello", end="_") 
print(name)
