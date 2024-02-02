# 5) WAP which finds out whether a given name is present in a list or not
nameList = ["Amruta", "Harry", "Ron", "Hermione", "Luna"]
nameInput = input("Enter a name to check in the list: ")

if nameInput in nameList:
    print("Sorry! Name already exists.")
else:
    nameList.append(nameInput)
    print("Name added successfully")
    print("Updated list:", nameList)


# OR DO THIS 
# listLen = len(nameList)
# found = False
# for i in range(0, listLen):
#     if (nameInput == nameList[i]):
#       found = True

# if(found):
#     print("Sorry, the name already exists.")
# else:
#    nameList.append(nameInput)
#    print("Name added successfully!")
#    print("Updated list:", nameList)