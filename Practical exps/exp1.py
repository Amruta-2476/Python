def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    if y == 0:
        print("Cannot divide by zero")
        return None
    else:
        return x / y

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print("1. Addition, 2. Subtraction, 3. Multiplication, 4. Division")
choice = int(input("Enter your choice: "))

if choice == 1:
    print("Addition is", add(x, y))
elif choice == 2:
    print("Subtraction is", sub(x, y))
elif choice == 3:
    print("Multiplication is", mul(x, y))
elif choice == 4:
    print("Division is", div(x, y))
else:
    print("Invalid choice")



