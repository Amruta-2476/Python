# import random

# movies = ['3 idiots', 'stree', 'munjya', 'queen', 'sholay', 'dangal', 'titanic', 'avengers', 'inception', 'interstellar']

# def create_question(movie):
#     n = len(movie)
#     letters = list(movie)
#     temp = []
#     for i in range(n):
#         if letters[i] == ' ':
#             temp.append(' ')
#         else:
#             temp.append('*')
#     qn = ''.join(str(x) for x in temp)
#     return qn

# def is_present(letter, movie):
#     c = movie.count(letter)
#     return c > 0

# def unlock(qn, movie, letter):
#     ref = list(movie)
#     qn_list = list(qn)
#     n = len(movie)
#     temp = []
#     for i in range(n):
#         if ref[i] == ' ' or ref[i] == letter:
#             temp.append(ref[i])
#         else:
#             if qn_list[i] == '*':
#                 temp.append('*')
#             else:
#                 temp.append(ref[i])
#     new_qn = ''.join(str(x) for x in temp)
#     return new_qn

# def play():
#     p1Name = input("Player 1: Enter your name: ")
#     p2Name = input("Player 2: Enter your name: ")
#     p1_points = 0
#     p2_points = 0
#     turn = 0
#     willing = True
#     while willing:
#         if turn % 2 == 0:
#             # player 1
#             print(p1Name, 'your turn')
#             picked_movie = random.choice(movies)
#             qn = create_question(picked_movie)
#             print(qn)
#             modified_qn = qn
            
#             not_said = True
#             while not_said:
#                 letter = input("Your letter: ")
#                 if is_present(letter, picked_movie):
#                     # unlock
#                     modified_qn = unlock(modified_qn, picked_movie, letter)
#                     print(modified_qn)
#                     d = int(input('Press 1 to guess movie or 2 to unlock another letter: '))
#                     if d == 1:
#                         ans = input('Your answer: ')
#                         if ans.lower() == picked_movie.lower():
#                             p1_points += 1
#                             print('Correct')
#                             not_said = False
#                             print(p1Name, 'your score:', p1_points)
#                         else:
#                             print('Wrong answer')
#                 else:
#                     print(letter, 'not found')
#             c = int(input('Press 1 to continue or 0 to quit: '))
#             if c == 0:
#                 print(p1Name, 'your score:', p1_points)
#                 print(p2Name, 'your score:', p2_points)
#                 print('Thanks for playing')
#                 willing = False
#         else:
#             # player 2
#             print(p2Name, 'your turn')
#             picked_movie = random.choice(movies)
#             qn = create_question(picked_movie)
#             print(qn)
#             modified_qn = qn
            
#             not_said = True
#             while not_said:
#                 letter = input("Your letter: ")
#                 if is_present(letter, picked_movie):
#                     # unlock
#                     modified_qn = unlock(modified_qn, picked_movie, letter)
#                     print(modified_qn)
#                     d = int(input('Press 1 to guess movie or 2 to unlock another letter: '))
#                     if d == 1:
#                         ans = input('Your answer: ')
#                         if ans.lower() == picked_movie.lower():
#                             p2_points += 1
#                             print('Correct')
#                             not_said = False
#                             print(p2Name, 'your score:', p2_points)
#                         else:
#                             print('Wrong answer')
#                 else:
#                     print(letter, 'not found')
#             c = int(input('Press 1 to continue or 0 to quit: '))
#             if c == 0:
#                 print(p1Name, 'your score:', p1_points)
#                 print(p2Name, 'your score:', p2_points)
#                 print('Thanks for playing')
#                 willing = False
#         turn += 1

# play()







import random

movies = ['3 idiots', 'stree', 'munjya', 'queen', 'sholay', 'dangal', 'titanic', 'avengers', 'inception', 'interstellar']

def create_question(movie):
    return ''.join([' ' if letter == ' ' else '*' for letter in movie])

def unlock(qn, movie, letter):
    return ''.join([letter if movie[i] == letter else qn[i] for i in range(len(movie))])

def play():
    p1Name = input("Player 1: Enter your name: ")
    p2Name = input("Player 2: Enter your name: ")
    scores = {p1Name: 0, p2Name: 0}
    players = [p1Name, p2Name]
    turn = 0
    
    while True:
        current_player = players[turn % 2]
        print(f"{current_player}, your turn")
        picked_movie = random.choice(movies)
        qn = create_question(picked_movie)
        print(qn)
        
        while True:
            letter = input("Your letter: ")
            if letter in picked_movie:
                qn = unlock(qn, picked_movie, letter)
                print(qn)
                guess = input('Guess the movie or press Enter to continue unlocking letters: ').strip()
                if guess.lower() == picked_movie.lower():
                    scores[current_player] += 1
                    print('Correct!')
                    break
                elif guess:
                    print('Wrong answer')
            else:
                print(f"'{letter}' not found in the movie")
        
        if input('Press Enter to continue or type "quit" to stop: ').strip().lower() == "quit":
            break
        turn += 1
    
    print(f"\nFinal Scores:\n{p1Name}: {scores[p1Name]}\n{p2Name}: {scores[p2Name]}")
    print('Thanks for playing!')

play()
