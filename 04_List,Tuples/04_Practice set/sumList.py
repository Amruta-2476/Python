# 4) WAP to sum a list with 4 numbers
i1 = int(input("Enter item 1: "))
i2 = int(input("Enter item 2: "))
i3 = int(input("Enter item 3: "))
i4 = int(input("Enter item 4: "))
a = [i1,i2,i3,i4]
total = a[0] + a[1] +a[2] + a[3]
print("Then sum of items in the list is: ",total)

# OR YOU CAN USE .SUM()
print(sum(a))