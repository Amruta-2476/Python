# 4) WAP to find whether number is prime or not
number = int(input("Enter a number: "))
count = 0
for i in range(2, number):
    if (number % i) == 0:
        count +=1

if(count > 0):
    print("Number is composite")
else:
    print("Number is prime")


