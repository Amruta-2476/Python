# 3) WAP to detect double spaces in a string
# 4) replace doubles spaces from 3) with single spaces

text = input("Enter your name: ")
a = text.find("  ")
# print(a)

if (a!= -1):
#   print("yes there exist double spaces")
    print(text.replace("  ", " "))
else:
  print("no double spaces don't exist")


''' Enter your name: this  string  has  double  spaces
this string has double spaces '''