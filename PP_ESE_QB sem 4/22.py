def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        print("Cannot divide by zero")
        return None
    else:
        return a / b

while True:
    print("1.Addition, 2.Subtraction, 3.Multiplication, 4.Division, 5.End")
    choice = int(input("Enter your choice: "))
    
    if choice == 5:
        print("Exiting the calculator. Goodbye!")
        break
    
    if choice in [1, 2, 3, 4]:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        
        if choice == 1:
            print("Addition is", add(a, b))
        elif choice == 2:
            print("Subtraction is", sub(a, b))
        elif choice == 3:
            print("Multiplication is", mul(a, b))
        elif choice == 4:
            result = div(a, b)
            if result is not None:
                print("Division is", result)
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
