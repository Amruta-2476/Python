# Tuple is ordered and UNCHANGEABLE 
            # List was changeable
thistuple = ("apple", "banana", "cherry")
print(thistuple)
# thistuple[0]="mango"   #TypeError:'tuple' object does not support item assignment
# print(thistuple)         

t = (1,2,3,4,5)
print(t[1])
print("Length of tuple t = ",len(t))

# empty tuple
empty_tuple = ()
print(empty_tuple)

# tuple with single element
# To create a tuple with one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.
thistuple = ("apple",)  #comma after that one item
print(type(thistuple))
print(thistuple)

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))   #str
print(thistuple)

# Check if "apple" is present in the tuple:
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")




