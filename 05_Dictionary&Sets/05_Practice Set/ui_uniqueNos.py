# 2) WAP TO INPUT 8 NUMBERS FROM USER AND DISPLAY ALL THE UNIQUE NUMBERS ONCE
# unique is asked :: therefore use set as set doesn't allow duplicates
# NOTE:: INPUT NUMBERS ARES STRING, MAKE SURE TO CONVERT INTO INT
n1 = int(input("Enter number 1: "))
n2 = int(input("Enter number 2: "))
n3 = int(input("Enter number 3: "))
n4 = int(input("Enter number 4: "))
n5 = int(input("Enter number 5: "))
n6 = int(input("Enter number 6: "))
n7 = int(input("Enter number 7: "))
n8 = int(input("Enter number 8: "))

numSet = {n1,n2,n3,n4,n5,n6,n7,n8}
print(numSet)

'''OP =>
Enter number 1: 2
Enter number 2: 3
Enter number 3: 4
Enter number 4: 2
Enter number 5: 3
Enter number 6: 4
Enter number 7: 5
Enter number 8: 2
{2, 3, 4, 5}
'''

s = {19, "19", 19.0}
print(s)  #{'19', 19}