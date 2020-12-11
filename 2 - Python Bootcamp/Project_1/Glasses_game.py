# Initial list

# Shuffle list

# User Guess

# Check Guess

from random import shuffle


def shuffle_lst(mylist):
    shuffle(mylist)
    return mylist


def player_guess():
    guess = ''
    while guess not in ['0', '1', '2']:
        guess = input('Lets play, where it is the ball, 0, 1 or 2... :')
    return int(guess)



def check_guess(mylist, guess):
    if mylist[guess] == 'O':
        print('You win!')
    else:
        print('You loose...')
        print(lst)


# Initial list
lst = [' ', 'O', ' ']

# Shuffle list
mixed_lst = shuffle_lst(lst)

# User Guess
user_guess = player_guess()

# Check Guess
check_guess(mixed_lst, user_guess)