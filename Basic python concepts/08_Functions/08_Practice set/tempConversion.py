# 2) WAP to convert celcius to farheneit

def  fahrenheit(cel):
    return  (cel * 9/5) +  32
c = float(input("Enter the temperature in celcius: "))
f = fahrenheit(c)
print ("Temperature in Fahrenheit is : ", f )