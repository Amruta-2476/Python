# 2) WAP to accept marks of 6 students and display them in a sorted manner
s1 = int(input("Enter marks of student 1: "))
s2 = int(input("Enter marks of student 2: "))
s3 = int(input("Enter marks of student 3: "))
s4 = int(input("Enter marks of student 4: "))
s5 = int(input("Enter marks of student 5: "))
s6 = int(input("Enter marks of student 6: "))
marksList = [s1,s2,s3,s4,s5,s6]

marksList.sort()
# display sorted order
print("Marks of students in sorted order: ", marksList)


# using for loop
# marksList = []
# for s in range(6):
#     marks = int(input(f"Enter marks of student {s+1}: "))
#     marksList.append(marks)
# print(marksList)
# marksList.sort()
# # display sorted order
# print("Marks of students in sorted order: ", marksList)