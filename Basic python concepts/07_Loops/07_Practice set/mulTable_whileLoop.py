# 3) WAP to print multiplication table using while loop
number = int(input("Enter the number whose table you want: "))
i = 1
while i <=10:
    print(f"{number} x {i} = {number * i}")
    i += 1