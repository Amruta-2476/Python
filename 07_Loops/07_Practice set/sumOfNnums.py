# 5) WAP to find sum of first n natural numbers using while loop
n = int(input("Enter a number: "))
i = 1
sum = 0
while (i <= n):
    sum = sum + i
    i += 1
print("The sum is : ",sum)