# Python has a set of built-in string methods 
story = "    HARRY POTTER"

# 1) len(str)
print(len(story))  # 12

# 2) .upper()  and   .lower()
print(story.upper())
print(story.lower())

# 3) .isUpper()  and  .isLower()
print(story.isupper())
print(story.islower())

# 4) .endswith("--")
print(story.endswith("ER",14, 16))   #or just (story.endswith("ER"))

# 5) .strip()
print(story.strip())    

# 6) .replace("--", "-")
print(story.replace(" ", ""))      #removes all spaces from the story
print(story.replace("H", "J")) 

# 7) .split()
story2 = "Harry Potter, Deathly Hallows"
print(story2.split())   # ['Goblet', 'of', 'Fire']
print(story2.split(","))  #splits at , 
txt = "apple#banana#cherry#orange"
print(txt.split("#"))   #['apple', 'banana', 'cherry',

# 8) .count()
print(story2.count('a'))       #how many times does 'a' appear in the string

# 9) .find()
print(story2.find('r'))        # 2 => first occurence

# STRING METHODS:
'''
+---------------------------+---------------------------------------------------------------------+
| Method                    | Description                                                         |
+---------------------------+---------------------------------------------------------------------+
| len(str)                  | Returns the length of the string.                                   |
+---------------------------+---------------------------------------------------------------------+
| .upper(), .lower()        | Converts all uppercase letters to lowercase or vice versa.          |
+---------------------------+---------------------------------------------------------------------+
| .islower(), .isupper()    | Returns True if all characters in the string are lower / upper case |
+---------------------------+---------------------------------------------------------------------+
| .endswith("--")           | Returns true if the string ends with the value specified in the     |
|                           |  parentheses, otherwise returns False.                              |
+---------------------------+---------------------------------------------------------------------+
| .strip()                  | removes any whitespace from the beginning or the end, trim          |
+---------------------------+---------------------------------------------------------------------+
| .replace("--", "-")       | replaces a string with another string                               |
+---------------------------+---------------------------------------------------------------------+
| find(value, start=0,      | Searches the string for a specified value and returns the           |
|        end=None)          | position of where it was found                                      |
|                           | if it's not found, it returns -1.                                   |
+---------------------------+---------------------------------------------------------------------+
| count()                   | Returns the number of times a specified value occurs in a string    |
+---------------------------+---------------------------------------------------------------------+
| .split(separator="",      | Splits the string at the specified separator, and returns a list.   |
|        max_splits=-1)     | By default, splits are done at each occurrence of the               |
|                           | separator. You can specify a maximum number of splits with          |
|                           | max_splits. An empty string ("") as the separator means split at    |
|                           | each character.                                                     |
+---------------------------+---------------------------------------------------------------------+
'''

'''
capitalize()	Converts the first character to upper case
casefold()	Converts string into lower case
center()	Returns a centered string

encode()	Returns an encoded version of the string

expandtabs()	Sets the tab size of the string

format()	Formats specified values in a string
format_map()	Formats specified values in a string
index()	Searches the string for a specified value and returns the position of where it was found
isalnum()	Returns True if all characters in the string are alphanumeric
isalpha()	Returns True if all characters in the string are in the alphabet
isascii()	Returns True if all characters in the string are ascii characters
isdecimal()	Returns True if all characters in the string are decimals
isdigit()	Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier

isnumeric()	Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable
isspace()	Returns True if all characters in the string are whitespaces
istitle()	Returns True if the string follows the rules of a title

join()	Converts the elements of an iterable into a string
ljust()	Returns a left justified version of the string

lstrip()	Returns a left trim version of the string
maketrans()	Returns a translation table to be used in translations
partition()	Returns a tuple where the string is parted into three parts

rfind()	Searches the string for a specified value and returns the last position of where it was found
rindex()	Searches the string for a specified value and returns the last position of where it was found
rjust()	Returns a right justified version of the string
rpartition()	Returns a tuple where the string is parted into three parts
rsplit()	Splits the string at the specified separator, and returns a list
rstrip()	Returns a right trim version of the string

splitlines()	Splits the string at line breaks and returns a list
startswith()	Returns true if the string starts with the specified value

swapcase()	Swaps cases, lower case becomes upper case and vice versa
title()	Converts the first character of each word to upper case
translate()	Returns a translated string

zfill()	Fills the string with a specified number of 0 values at the beginning
'''