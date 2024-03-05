# 2) wap to make a game function that returns the score as an integer. you need to read a file 'Highscore.txt' which contains previous HighScore. you need to write a program to update the highScore whenever game() breaks the highScore

def game():
    return 596

with open('highScore.txt') as f:
    # print(f.read())  # => 39
    high_score = int(f.read())
    if (game()) > high_score:
        f = open('highScore.txt', 'w')
        f.write(str(game()))
# 7:35:00