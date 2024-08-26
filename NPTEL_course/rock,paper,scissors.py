# the catch here is that no cheating is allowed 
# there will be 2 players 
# they will hide their choice in a 10 digit number so that the other player cannot see it, and a secret bit where the choice is stored

def rock_paper_scissors(num1, num2, bit1, bit2):
   p1 = int(num1[bit1]) % 3   # p1 is the bit position bit1 of num1, and mod 3 so that we get number like 0,1,2
   p2 = int(num2[bit2]) % 3 
   if (player_one[p1] == player_two[p2]):
      print("Draw")
   elif (player_one[p1] == 'rock' and player_two[p2] == 'scissors'):
      print("Player 1 wins")
   elif (player_one[p1] == 'rock' and player_two[p2] == 'paper'):
        print("Player 2 wins")
   elif (player_one[p1] == 'paper' and player_two[p2] == 'scissors'):
        print("Player 2 wins")
   elif (player_one[p1] == 'paper' and player_two[p2] == 'rock'):
        print("Player 1 wins")
   elif (player_one[p1] == 'scissors' and player_two[p2] == 'rock'):
        print("Player 2 wins")
   elif (player_one[p1] == 'scissors' and player_two[p2] == 'paper'):
        print("Player 1 wins")
      


player_one = {0: 'rock', 1: 'paper', 2: 'scissors'}
player_two = {0: 'paper', 1: 'rock', 2: 'scissors'}
while(1):
    num1 = input("Player 1, enter your choice: ")
    num2 = input("Player 2, enter your choice: ")
    bit1 = int(input("Player 1, enter your secret bit position: "))
    bit2 = int(input("Player 2, enter your secret bit position: "))
    rock_paper_scissors(num1, num2, bit1, bit2)
    ch = input("Do you want to continue? y/n: ")
    if (ch == 'n'):
        break