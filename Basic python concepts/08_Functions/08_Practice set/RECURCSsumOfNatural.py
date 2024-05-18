# 4) WAP using recursion to print sum of n natural numbers

def sum(n):
    if n<0:
        return n
    else:
        return n + sum(n-1)
    
num = int(input('Enter the number : '))
if num < 0:
    print("enter a positve integer !")
else:
    print('The sum is ',sum(num))