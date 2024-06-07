import file1
file1.greet('Ria')

# Output: 
# Enter your name: 
# why do we get this output?
# because the entire code in m01.py is executed when we import it in m02.py
# so the input() function is executed and we get the output "Enter your name: "

# to avoid this we use the following code in m01.py
# if __name__ == '__main__':
#     n = input("Enter your name: ")
#     greet(n)
# this way the code inside the if block will only be executed when we run m01.py and not when we import it in m02.py
# so we will not get the output "Enter your name: " when we import file1.py in file2.py


'''  Here __name__ == file1
Therefore output is only
Hello, Ria '''