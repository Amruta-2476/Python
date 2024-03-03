# SIMILARLY YOU CAN DO ROCK PAPER SCISSORS
'''
Snake (s) beats Water (w) - Snake drinks water.
Water (w) beats Gun (g) - Water destroys the gun.
Gun (g) beats Snake (s) - Gun kills the snake.'''
a = input("Player 1: Snake(s), Water(w) or Gun(g) ? ")
b = input("Player 2: Snake(s), Water(w) or Gun(g) ? ")

# logic to determine the winner
if a == b:
    print ("It's a tie!")
elif a =='s':
    if b=="w":
        print("Player 1 wins! Snake drinks water.")
    elif b=="g":
        print("Player 2 wins! Gun kills the snake.")
elif a == 'w':
    if b == 's':
        print("Player 2 wins! Snake drinks water.")
    elif b == 'g':
        print("Player 1 wins! Water destroys the gun.")
elif a == 'g':
    if b == 's':
        print("Player 1 wins! Gun kills the snake.")
    elif b == 'w':
        print("Player 2 wins! Water destroys the gun.")
else:
    print("Invalid input. Please choose s, w, or g.")

