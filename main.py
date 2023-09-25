import random


def get_winner(p1, p2):
    if p1 == p2:
        return 0
    elif p1 == 'rock':
        if p2 == 'scissors':
            return 1
        else:
            return 0
    elif p1 == 'paper':
        if p2 == 'rock':
            return 1
        else:
            return 0
    elif p1 == 'scissors':
        if p2 == 'paper':
            return 1
        else:
            return 0


computer_wins = 0
human_wins = 0

while computer_wins < 3 and human_wins < 3:
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    human_choice = input('Enter your choice (rock, paper, scissors): ')

    try:
        computer_wins += get_winner(computer_choice, human_choice)
        human_wins += get_winner(human_choice, computer_choice)
    except:
        print('Invalid choice! Please try again.')
        break

    print('Computer\'s choice:', computer_choice)
    print('Computer\t:\tHuman')
    print('\t', computer_wins, '\t\t:\t', human_wins)

    if computer_wins >= 3:
        print('Computer wins!')
    elif human_wins >= 3:
        print('Human wins!')
