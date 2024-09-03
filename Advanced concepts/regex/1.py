import re
# The search() function searches for specified patterns within a string. Here is an example that explains how to use the search() function to search for the word "Jackson" in the string "Michael Jackson is the best".

s1 = "Michael Jackson is the best"

# Define the pattern to search for
pattern = r"Jackson"

# Use the search() function to search for the pattern in the string
result = re.search(pattern, s1)

# Check if a match was found
if result:
    print("Match found!")
else:
    print("Match not found.")



pattern = r"\d\d\d\d\d\d\d\d\d\d"  # Matches any ten consecutive digits
text = "My Phone number is 1234567890"
match = re.search(pattern, text)

if match:
    print("Phone number found:", match.group())
else:
    print("No match")
# The regular expression pattern is defined as r"\d\d\d\d\d\d\d\d\d\d", which uses the \d special sequence to match any digit character (0-9), and the \d sequence is repeated ten times to match ten consecutive digits



pattern = r"\W"  # Matches any non-word character
text = "Hello, world!"
matches = re.findall(pattern, text)

print("Matches:", matches)

# The regular expression pattern is defined as r"\W", which uses the \W special sequence to match any character that is not a word character (a-z, A-Z, 0-9, or _). The string we're searching for matches in is "Hello, world!".


# The findall() function finds all occurrences of a specified pattern within a string.
s2 = "Michael Jackson was a singer and known as the 'King of Pop'"
# Use the findall() function to find all occurrences of the "as" in the string
result = re.findall("as", s2)

# Print out the list of matched words
print(result)



# A regular expression's split() function splits a string into an array of substrings based on a specified pattern.
# Use the split function to split the string by the "\s"
split_array = re.split("\s", s2)

# The split_array contains all the substrings, split by whitespace characters
print(split_array) 



# The sub function of a regular expression in Python is used to replace all occurrences of a pattern in a string with a specified replacement.
# Define the regular expression pattern to search for
pattern = r"King of Pop"

# Define the replacement string
replacement = "legend"

# Use the sub function to replace the pattern with the replacement string
new_string = re.sub(pattern, replacement, s2, flags=re.IGNORECASE)

# The new_string contains the original string with the pattern replaced by the replacement string
print(new_string) 