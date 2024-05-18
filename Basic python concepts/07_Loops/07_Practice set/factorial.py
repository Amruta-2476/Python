# 6) WAP to calculate factorial using for loop
x = int(input("Enter a number: "))
# x! = x.(x-1).(x-2)....1
# x! = x.(x-1)!

fact = 1
if x == 0 or x == 1 :
    print(f"Factorial of {x} is 1")
else:
  for i in range (1, x+1):
      fact = fact * i
  print(f"Factorial of {x} is {fact}")