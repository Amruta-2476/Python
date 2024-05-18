# workaround to update a tuple
#   > convert the tuple into a list
#   > change the list
#   > convert the list back into a tuple
myTuple = ("apple", "banana", "cherry")
y = list(myTuple)  #converted tuple to list

y.append("pineapple")   #updated the list
myTuple = tuple(y)   #converted the updated list back into tuple
print(myTuple)

# OR 
# WE CAN CREATE A NEW TUPLE WITH THE ITEM THAT WE WANT TO ADD. 
# THEN WE ADD THE NEW TUPLE TO THE ORIGINAL TUPLE
fruitTuple = ("apple","cherry","kiwi")
newTup = ("peach",)
fruitTuple += newTup    
print(fruitTuple)

# 1) convert tuple to list, update that list, convert back into tuple 
# 2) Add the new tuple to the original tuple


# REMOVE ITEMS FROM TUPLE: 
# > convert tuple to list
# > list.remove("item") 
# > convert back into tuple
myTuple2 = ("apple", "banana", "cherry")
y = list(myTuple2)  #converted tuple to list

y.remove("cherry")   #updated the list
myTuple2 = tuple(y)   #converted the updated list back into tuple
print(myTuple2)

