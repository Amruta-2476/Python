# 7) WAP a function to remove a given word from the list and strip it
# strip = trim extra white spaces leading and trailing
def remove_strip(thisList, word, word_to_strip):
    thisList.remove(word)
    strippedWord = word_to_strip.strip()
    return strippedWord

myList = ["apple", "mango", "  cherry   ", "kiwi"]
print("befor:",myList)

remove_this_word = "mango"
strip_this_word = "  cherry   "

newList = remove_strip(myList, remove_this_word, strip_this_word)
print("After: ",myList)
print("After stripping the word: ", newList)