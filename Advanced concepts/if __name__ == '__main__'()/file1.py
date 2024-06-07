def greet(name): 
    print("Hello, " + name)

'''n = input("Enter your name: ")
greet(n)'''
# Output: 
# Enter your name: John
# Hello, John

# lets say we want to use this function in another file/module m02.py 

print(__name__)     # Output: __main__
if __name__ == '__main__':
    n = input("Enter your name: ")
    greet(n)
    print('this is file1.py')