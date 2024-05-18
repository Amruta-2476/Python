# 1)WAP using function to find greatest of the 3 numbers
def greatest(a,b,c):
    if a>b and a>c:
        print("The greatest number is",a)
    elif b>a and b>c:
        print("The greatest number is",b)
    else:
        print("The greatest number is",c)

#  or
    # if a>b :
    #     if(a>c):
    #         return a
    #     else:
    #         return c
    # else:
    #     if(b>c):
    #         return b
    #     else:
    #         return c

x = int(input("enter 1st no.: "))
y = int(input("enter 2nd no.: "))
z = int(input("enter 3rd no.: "))
greatest(x, y, z)
# max = greatest(x, y, z)
# print(max)