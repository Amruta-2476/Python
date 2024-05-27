# Open file for writing the data
with open("data.txt", "w") as data:
    string = input("Enter a string to write into the file: ")
    data.write(string)
# For reading the character from the file
with open("data.txt", "r") as data:
    print("Content of the file:")
    print(data.read())

# Open file for appending data
with open("data.txt", "a") as data:
    string_to_append = input("Enter a string to append to the file: ")
    data.write("\n" + string_to_append)
# Open file for reading appended content
with open("data.txt", "r") as data:
    print("Appended content of the file:")
    print(data.read())

# Deleting the contents of the file
with open("data.txt", "w") as data:
    data.write("")
# reading the file after deleting the content
with open("data.txt", "r") as data:
    print("Content of the file after deleting:")
    print(data.read())
