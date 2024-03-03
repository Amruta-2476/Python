# 5) WAP TO PRINT THIS:
'''
* * *
* *
*    n=3
'''
# def starPattern(n):
#     for i in range(n, 0, -1):
#         for j in range(i, 0, -1):
#            print("*", end=" ")
#         print(" ")


# OR W/0 USING FUNCTION
n=3
for i  in range(n):
    print("*" *(n-i))

# num = int(input("enter a number:"))
# starPattern(num)