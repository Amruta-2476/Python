# List Methods:
list2 = ["Harry", "Hermione", "Ana", "Ben"]
list2.sort()
print("Sorted list: ", list2)
print(len(list2))

list1 = [1, 3, 6, 2, 95, 43, 4]
list1.sort()     #[1, 2, 3, 4, 6, 43, 95]
list1.reverse()     #[4, 43, 95, 2, 6, 3, 1]
indexNum = list1.index(6)
print("Index of 6 in the list is: ", indexNum)

list1.append(8)   #[1, 3, 6, 2, 95, 43, 4, 8]  #imp
list1.insert(3, 1000)   #[1, 3, 6, 1000, 2, 95, 43, 4]
list1.extend(list2)  #[1, 3, 6, 2, 95, 43, 4, 'Ana', 'Ben', 'Harry', 'Hermione'] 

list1.pop(2)   #[1, 3, 2, 95, 43, 4]

del list1[1]    #[1, 6, 2, 95, 43, 4]
list1.remove(4)  #[1, 6, 2, 95, 43]

print(list1)

# copy the list using list()
l1 = [1,2,3,4,5]
l2 = list(l1)  # The list() function to create a copy of l1
l1[0] = 22
print(l1)  # Output: [22, 2, 3, 4, 5]
print(l2)  # Output: [1, 2, 3, 4, 5]
# modify l1, it doesn't affect the contents of l2, because they are different lists

