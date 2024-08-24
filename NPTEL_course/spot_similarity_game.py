# look at another way for this

import string
import random
# print(string.ascii_letters)  # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ

symbols = []
symbols = list(string.ascii_letters)
print(symbols) 
# ['a', 'b', 'c', 'd', 'e', 'f', 'g' .. 'A', 'B' ... ]

card1 = [0] * 5   # list with 5 0s
card2 = [0] * 5   # list with 5 0s

pos1 = random.randint(0, 4)
pos2 = random.randint(0, 4)
print(pos1, pos2)
# pos1 and pos2 are the same symbol positions in card1 and card2

same_symbol = random.choice(symbols)
symbols.remove(same_symbol) # remove the same symbol from the list
if pos1 == pos2:
    card2[pos2] = same_symbol
    card1[pos2] = same_symbol
else:
    card1[pos1] = same_symbol
    card2[pos2] = same_symbol
    card1[pos2] = random.choice(symbols)
    symbols.remove(card1[pos2])
    card2[pos1] = random.choice(symbols)
    symbols.remove(card2[pos1])

i = 0
while i < 5:
    if (i != pos1 and i != pos2):
        alphabet1 = random.choice(symbols)
        symbols.remove(alphabet1)
        alphabet2 = random.choice(symbols)
        symbols.remove(alphabet2)
        card1[i] = alphabet1
        card2[i] = alphabet2
    i += 1
print(card1)
print(card2)
ch = input("Spot the similar symbol: ")
if ch == same_symbol:
    print("Right")
else:
    print("Wrong")