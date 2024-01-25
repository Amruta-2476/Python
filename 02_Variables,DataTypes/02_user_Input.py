a = input("enter your name: ")
print(a)

b=input("enter a number: ")
print(b)
print(type(b))

## As we saw b input was a str so if we try to do arithmetic operation on it python will give an error. So, we need to convert the data type of b into int
# > print("sum of b and 4 is: ",(b+4))
# TypeError: can only concatenate str (not "int") to str 
# as it considers b as a str

print("")
#converting str 'b' to integer
b=int(b)
print(b)
print(type(b))
print("sum of b and 4 is: ",(b+4))

# or just o this:
# b=input("enter a number: ")
# b=int(b)
# print(b)