# SIMILARLY YOU CAN DO ROCK PAPER SCISSORS
import random

def game(comp, you):
    if comp == you:
        return None
    elif comp == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True
    elif comp == 'g':
        if you == 's':
            return False
        elif you == 'w':
            return True
    elif comp == 'w':
        if you == 's':
            return True
        elif you == 'g':
            return False

print("Computer's turn: Snake(s), Water(w) or Gun(g) ? ")
choiceList = ['s', 'w', 'g']
computerChoice = random.choice(choiceList)
# selects random choice from the given sequence
yourChoice= input("Your turn: Snake(s), Water(w) or Gun(g) ? ")

outcome = game(computerChoice, yourChoice)
if outcome == None:
    print("It's a tie")
elif outcome == True:
    print("You win!")
else:
    print("You lose...")

print("You chose: ",yourChoice)
print("Computer chose: ",computerChoice)