# 1) WAP to print table of a number using for loop
number = int(input("Enter the number whose table you want: "))

for i in range(1, 11):
    print(f"{number} X {i} = {number * i}")