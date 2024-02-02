# 1) WAP to create a dictionary of hindi words with values as their english translation. Provide user input for the word and display its corresponding English Translation.

hindiDict = {
    "Pankha":"Fan",
    "Khana":"Food",
    "Dabba":"Box",
}
print("Options are: ",hindiDict.keys())
a = input("Enter the Hindi Word: ")
print(f"{a} in English means {hindiDict[a]}")

# if a in hindiDict:
#     print("yes its there!")
#     print(f"{a} in English means {hindiDict[a]}")
# else:
#     print("Sorry, no such word in the dictionary")