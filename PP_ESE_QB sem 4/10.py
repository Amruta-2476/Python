# Explain bitwise operators of python with suitable examples of each.

# Bitwise operators in Python are used to perform bitwise operations on integers. 
# The integers are first converted into binary and then operations are performed on bit by bit, hence the name bitwise operators.
# These operators treat operands as sequences of binary digits (bits) and perform operations bit by bit. 
# Here are the bitwise operators available in Python:


# 1. Bitwise AND (&): 
# returns 1 if both bits are 1, otherwise 0.
# Example:
a = 5  # 101 in binary
b = 3  # 011 in binary
result = a & b  # Result: 1
print("Bitwise AND:", result)  # Output: 1 (001 in binary)



# 2. Bitwise OR (|): 
# It returns 1 if at least one of the bits is 1, else 0.
# Example:
a = 5  # 101 in binary
b = 3  # 011 in binary
result = a | b  # Result: 7
print("Bitwise OR:", result)  # Output: 7 (111 in binary)



# 3. Bitwise XOR (^): 
# It returns 1 if the bits are different, otherwise 0.
# Example:
a = 5  # 101 in binary
b = 3  # 011 in binary
result = a ^ b  # Result: 6
print("Bitwise XOR:", result)  # Output: 6 (110 in binary)



# 4. Bitwise NOT (~): 
# Flips all the bits of an integer, i.e., changes 1s to 0s and vice versa. It's a unary operator.
# Example:
a = 5  # 101 in binary
result = ~a  # Result: -6
print("Bitwise NOT:", result)  # Output: -6 (complement of 101 is 010, which is -6 in 2's complement)



# 5. Left Shift (<<): 
# Shifts the bits of the first operand to the left by the number of positions specified by the second operand. 
# Zeros are shifted in from the right.
# Example:
a = 5  # 101 in binary
result = a << 2  # Result: 20
print("Left Shift:", result)  # Output: 20 (10100 in binary)



# 6. Right Shift (>>): 
# Shifts the bits of the first operand to the right by the number of positions specified by the second operand. 
# Zeros are shifted in from the left. 
# Example:
a = 20  # 10100 in binary
result = a >> 2  # Result: 5
print("Right Shift:", result)  # Output: 5 (101 in binary)



# These bitwise operators are useful in low-level programming, cryptography, 
# and optimization tasks where manipulation of individual bits is required.