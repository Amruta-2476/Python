# take only even numbers from list a
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = []
for item in a:
    if item % 2 == 0:
        b.append(item)
print(b)

# OR : using list comprehension: make list b in one line
# basically shortcut of above code
# list comprrehension : to create a list based on existing list
b = [item for item in a if item % 2 == 0]
print(b)

# similarly can do set and dictionary comprehensions as well
# set comprehension : no repeated values
list1 = [1, 2, 4, 2, 1 , 5, 6, 8, 1, 5]
set = {item for item in list1}
print(set)

# dictionary comprehension : key value pair
