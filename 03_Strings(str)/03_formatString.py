# age = 36
# txt = "My name is John, I am " + age
# print(txt)
# we cannot combine strings and numbers like this

# But we can combine strings and numbers by using the format() method!
# The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} are:

quantity = 3
itemNo = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemNo, price))
# OR
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemNo, price))