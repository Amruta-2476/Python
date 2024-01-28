# Creating empty set and then adding elements in it using .add()
c = set()
print(type(c))

# 1) .add() method
c.add(4)
c.add(5)
c.add(5)
# c.add([1,2,3])  #TypeError: unhashable type: 'list'. Cannot add list in set coz list is changeable but set is unchangeable
# we cannot add dict either
# c.add({4:67})   #TypeError: unhashable type: 'dict'

# but we can add tuple as tuple is also unchangeable
c.add((1,2,3))  # {(1, 2, 3), 4, 5}
print(c)

# 2) len(<set>)
print(len(c))

# 3) .update(newSet)
newSet = { 99, 88 }
c.update(newSet)  #{99, 4, 5, 88, (1, 2, 3)}
print(c)

# 4) .remove(x) - removes the first occurrence of x 
c.remove(5)
print(c)

# 5) .pop() - removes any random item
itemPopped = c.pop()
print("Item Popped : ",itemPopped)
print("After Pop : ",c)

# 6) .clear() -empties the set
c.clear()
print(c)