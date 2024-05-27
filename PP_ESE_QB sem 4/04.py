# What will be output of the following program and also explain the type of error if any.
try:
    list=[1,2,3,4,5]
    print(list[2])
    print(list[5])
except:
    print ("Error: Index out of range.")

# Output: 3
# Error: Index out of range.
'''
Index Error:
In the try block, there are two print statements trying to access elements of the list list.
print(list[2]): Accesses the element at index 2, which is 3.
print(list[5]): Tries to access the element at index 5, which is beyond the range of the list.
Accessing an index that is out of range of the list raises an IndexError.
Error Type:

The error raised in this case is an IndexError.
This error occurs when you try to access an index that is out of range for the given list, tuple, or other sequence types.
It is a runtime error that is raised when the interpreter encounters such a situation during program execution.
Output:

The first print statement (print(list[2])) executes successfully and prints 3, which is the element at index 2.
The second print statement (print(list[5])) raises an IndexError, and the exception handling block (except) catches it.
The print statement inside the except block is then executed, which prints "Error: Index out of range.".
'''