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

# Counting number of lines, words, and characters in a file
with open("data.txt", "r") as data:
    if data:
        lines = data.readlines()
        num_lines = len(lines)
        num_words = sum(len(line.split()) for line in lines)
        num_chars = sum(len(line) for line in lines)
        print("Number of lines:", num_lines)
        print("Number of words:", num_words)
        print("Number of characters:", num_chars)
    else:
        print("File does not exist.")


