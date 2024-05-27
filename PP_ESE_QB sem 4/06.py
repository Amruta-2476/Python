'''
### Python Assignment Operators

Assignment operators in Python are used to assign values to variables. The most common assignment operator is the equal sign (`=`), which assigns the value on the right to the variable on the left. In addition to the basic assignment operator, Python provides several compound assignment operators that perform an operation and assign the result in one step.

#### Basic Assignment Operator:
- `=`: Assigns the value on the right to the variable on the left.
  ```python
  x = 10
  ```

#### Compound Assignment Operators:
- `+=`: Adds the right operand to the left operand and assigns the result to the left operand.
  ```python
  x += 5  # Equivalent to x = x + 5
  ```
- `-=`: Subtracts the right operand from the left operand and assigns the result to the left operand.
  ```python
  x -= 3  # Equivalent to x = x - 3
  ```
- `*=`: Multiplies the left operand by the right operand and assigns the result to the left operand.
  ```python
  x *= 2  # Equivalent to x = x * 2
  ```
- `/=`: Divides the left operand by the right operand and assigns the result to the left operand.
  ```python
  x /= 4  # Equivalent to x = x / 4
  ```
- `%=`: Performs modulus operation on the left operand with the right operand and assigns the result to the left operand.
  ```python
  x %= 3  # Equivalent to x = x % 3
  ```
- `**=`: Raises the left operand to the power of the right operand and assigns the result to the left operand.
  ```python
  x **= 2  # Equivalent to x = x ** 2
  ```
- `//=`: Performs floor division on the left operand by the right operand and assigns the result to the left operand.
  ```python
  x //= 2  # Equivalent to x = x // 2
  ```

### Python Arithmetic Operators

Arithmetic operators in Python are used to perform mathematical operations on numeric values. These operators include basic arithmetic operations such as addition, subtraction, multiplication, and division, as well as more advanced operations like exponentiation and modulus.

#### Basic Arithmetic Operators:
- `+`: Addition. Adds two operands.
  ```python
  result = 10 + 5  # result is 15
  ```
- `-`: Subtraction. Subtracts the right operand from the left operand.
  ```python
  result = 10 - 5  # result is 5
  ```
- `*`: Multiplication. Multiplies two operands.
  ```python
  result = 10 * 5  # result is 50
  ```
- `/`: Division. Divides the left operand by the right operand, resulting in a float.
  ```python
  result = 10 / 5  # result is 2.0
  ```
- `%`: Modulus. Returns the remainder when the left operand is divided by the right operand.
  ```python
  result = 10 % 3  # result is 1
  ```
- `**`: Exponentiation. Raises the left operand to the power of the right operand.
  ```python
  result = 2 ** 3  # result is 8
  ```
- `//`: Floor Division. Divides the left operand by the right operand and rounds down to the nearest integer.
  ```python
  result = 10 // 3  # result is 3
  ```

### Examples

Here's a combined example demonstrating the use of assignment and arithmetic operators:

```python
# Assignment operators
x = 10      # x is assigned 10
y = 5       # y is assigned 5

# Arithmetic operations
addition = x + y            # 15
subtraction = x - y         # 5
multiplication = x * y      # 50
division = x / y            # 2.0
modulus = x % y             # 0
exponentiation = x ** y     # 100000
floor_division = x // y     # 2

# Compound assignment operations
x += y    # x is now 15
x -= y    # x is now 10
x *= y    # x is now 50
x /= y    # x is now 10.0
x %= y    # x is now 0.0
x **= y   # x is now 0.0
x //= y   # x is now 0.0
```

These operators provide the basic tools needed to perform and manipulate arithmetic operations and manage variable assignments efficiently in Python.
'''