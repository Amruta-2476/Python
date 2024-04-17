num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

try :
  print(num1/num2)
except ZeroDivisionError as e:
  print("Exception occured:",e)
else :
  print("No exception occured")
finally :
  print("End of program")




