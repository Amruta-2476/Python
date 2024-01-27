myList = [1, 2, 3, 45, 6]  # ORDERED
print(myList)
# access first element
print(myList[0]) 

# we can change the elements
myList[0]=99   # CHANGEABLE
print("After changing first element:", myList)

# we can create a list with items of different data types
mixedTypeList = ["Hello", 78, True, None, 45.67]
print(mixedTypeList)

# List Slicing
print(mixedTypeList[ 0 : 3])  #excluding 3

# len()
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

# Check if "apple" is present in the list:
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

# Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon"
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)
