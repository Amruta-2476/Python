# 1) WAP to find greatest of 4 numbers
num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
num3 = int(input("Enter 3rd number: "))
num4 = int(input("Enter 4th number: "))

greatest = num1

# if num2 > greatest:
#     greatest = num2
# elif num3 > greatest:
#     greatest = num3
# else:
#     greatest = num4
# here if 1st if is true then it doesn't even check the rest, so we have to use different if's for each condition

if num2 > greatest:
    greatest = num2

if num3 > greatest:
    greatest = num3

if num4 > greatest:
    greatest = num4
print("The greatest number is:", greatest)
