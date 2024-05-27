# What will be output of the following program and also explain the type of error if any.
try:
    num = 10
    den = 0
    result = num/den
    print(result)
except:
    print ("Error: Denominator cannot be 0.")
'''
Division by Zero Error:
In the try block, there is a division operation num/den where den is assigned the value 0.
Division by zero is mathematically undefined, which raises a ZeroDivisionError.
Since the exception handling block (except) catches all exceptions (due to no specific exception type specified), it executes the print statement "Error: Denominator cannot be 0.".
Error Type:

The error raised in this case is a ZeroDivisionError.
This error occurs when you try to divide a number by zero, which is not allowed in mathematics.
It is a runtime error that is raised when the interpreter encounters such a situation during program execution.
Output:

The output of the program is the print statement inside the except block, which is "Error: Denominator cannot be 0.".
'''