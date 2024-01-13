# 2) WAP TO FIND REMAINDER WHEN A NUMBER IS DIVIDED BY 2
x=input("Enter a number: ")
x=int(x)
print("Num1 = ",x)

print("The remainder when divided by 2 is:",(x%2))

# even and odd program
if (x%2) == 0:
    print("x is even")
else:
    print("x is odd")