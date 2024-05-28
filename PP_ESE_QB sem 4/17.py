try:
    result = int(input("Enter a number: ")) / 0
    print("Result:", result)
    list = [1,2,3,4,5]
    print(list[10])
except ValueError:
    # ValueError = if the input cannot be converted to an integer
    print("Error: Invalid input. Please enter a valid number.")

except ZeroDivisionError:
    print("Error: Division by zero")

except Exception as e:
    # generic exception handling
    print("An error occurred:", e)
finally:
    # optional block, executed regardless of exception
    print("Finally block executed")
