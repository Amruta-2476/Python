# Python - Join Sets

# > .union() method that returns a new set3 containing all items from both set1 and set2, or 
set1 = {"a", "b" , "c", 3}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print("Set 1: ", set1)
print("Set 2: ", set2)
print("New set as a union of these two:",set3)

# > .update() method that inserts all the items from set2  into set1. If an item is present in both sets it will be included once.
setA = {"a", "b" , "c"}
setB = {1, 2, 3}
setA.update(setB)
print(setA)

# > .intersection() method returns a new set contains common elements between set1 and set2. If no common elements then return an empty set.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
new = x.intersection(y)
print(new)

# >.intersection_update(): intersection on the sets and update the original set with the result. No new set
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)

# > The difference between the sets is obtained using the .difference() method which returns a new set with items that are in one set but not the other. If you want to remove common elements
