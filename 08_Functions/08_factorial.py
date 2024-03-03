# n! = 1*2*3*4...*n
n = int(input("Enter a number: "))
# 0! and 1! = 1
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        result = n * factorial(n-1)
    return result
print("Factorial of ",n, "is", factorial(n))