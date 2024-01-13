a="3454"
print(a)
print(type(a))
a = float(a)
print('After type casting: ',type(a))
print(a+5)
# 3454
# <class 'str'>
# TypeError: can only concatenate str (not "int") to str

b="98fa88"
print(type(b))
b=int(b) #ValueError: invalid literal for int() with base 10: '98fa88'


# > TYPE CONVERSION
# int_var = int(98.65)
# float_var = float(98)
# str_var = str(98)
# list_var = list([1,2,3])
# tuple_var = tuple((1,2,3))
# dict_var = dict({'name':'John','age':25})
# print("Integer:",int_var,"\nFloat:",float_var,
#       "String:",str_var,"List:",list_var,
#       "Tuple:",tuple_var,"Dictionary:",dict_var)