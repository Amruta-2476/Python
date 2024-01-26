greeting = "Good Morning, "
name = "Amruta"
c = greeting + name  #concatenation
print(c)
print(name[2])
# name[2] = "d"  #cannot change a character in str like this
# TypeError: 'str' object does not support item assignment



# STRING SLICING:=
#  (str[ startIndex : (endIndex-1) ])
# You can return a range of characters by using the slice syntax.
# Specify the start index and the end index, separated by a colon, to return a part of the string.
b = "Hello, World!"
print(b[2:5])  # llo  #excluding 5 so , won't come

# a) if no start index then from 0 to given:
print(b[:5])   # Hello

# b) if no end index then from given to end:
print(b[4:])   # o, World!

# c) Negative indexes to start the slice from the end of the string:
print(b[-5:-2])   # orl
# From: "o" in "World!" (position -5)
# To, but not included: "d" in "World!" (position -2)

# d) Slicing with skip value
x = "amazingDayToday"   
# word[1:6] with a skip value of 2
print(x[ 1 : 6 : 2]) #mzn
print(x[ 0 :: 4 ])  #aiad

print(x[::3])    #'azgyd'
# It skips 3 steps at a time
print(x[::2])    # 'aaigaTdy'
# It skips 2 steps at a time








