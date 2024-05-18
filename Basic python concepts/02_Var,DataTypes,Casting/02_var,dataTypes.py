a="Amruta"
# python automatically identifies that this is a string literal by looking at the double quotes
print(a)
b=345
c=45.39
d=True
e=None

# printing the type of varables
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
'''Amruta
<class 'str'>
<class 'int'>
<class 'float'>
<class 'bool'>
<class 'NoneType'>'''

print('')
x='''Twinkle Twinkle little star
How I wonder what you are
Up above the world so high'''
print(x)

# casting c=45.39
y=int(c) # cast float to int, truncating decimal part
z=round(c) # rounding off the value of c to the nearest integer
w=str(c) # converting float to str
v=bool(c) # converting float to bool; So 0 becomes False and any other number true
print('')
print(y)
print(z)
print(w)
print(v)

# b=345
B='hola'  #python is case sensitive
print(b)
print(B)

'''
> Camel Case
Each word, except the first, starts with a capital letter:
myVariableName = "John"

> Pascal Case
Each word starts with a capital letter:
MyVariableName = "John"

> Snake Case
Each word is separated by an underscore character:
my_variable_name = "John" '''

price = 490
print(f"The price of mangoes is ${price}")
