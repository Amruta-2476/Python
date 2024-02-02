# 6) Create an empty dict. Allow 4 friends to enter their favourite language as values and use keys as their names. Assume that the names are unique

langDict = {}
print(type(langDict))   #<class 'dict'>
# for x in range(1,5):
#     a = input(f"Enter your name friend{x}: ")  #this is key
#     b = input(f"Hi {a}! Enter your fav lang: ")  #this is values
#     langDict[a] = b

# print(langDict)


# without using for loop
a = input("Enter your fav language Harry: ")
b = input("Enter your fav language Ron: ")
c = input("Enter your fav language Hermione: ")
d = input("Enter your fav language Hagrid: ")
langDict["Harry"] = a
langDict["Ron"] = b
langDict["Hermione"] = c
langDict["Hagrid"] = d
print(langDict)

