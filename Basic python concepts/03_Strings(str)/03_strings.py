b = "Amruta"
print(b, type(b))
c = '''Mary 
       had a
       little lamb'''
print(c)


# 1) Access one element of the string using [index]
a = "Hello, World!"
print("element at index 1 is:",a[1])   # e


# 2) Looping Through a String using 'for' loop
for x in "apple":
  print(x) 


# 3) The len() function returns the length of a string
a = "Hello, World!"  #13
print(len(a))


# 4) To check if a certain phrase / character is present in a string, we can use the keyword 'in'
fruit = "orange"
if "an" in fruit:
  print("Yes")  # Yes
else:
  print("No")

txt = "The best things in life are free!"
print("free" in txt)   #True


# 5) Check if a certain phrase or character is NOT present in a string, we can use the keyword 'not in'
txt = "The best things in life are free!"
print("expensive" not in txt)  #True


# 6) We can also find out how many times a substring appears in a given string using count()
print(txt.count("e"))    #6


# 7) Splitting a string into components using split() method
s = "This is a sample sentence."
words = s.split()
print(words)   #['This', 'is', 'a', 'sample', 'sentence.']



