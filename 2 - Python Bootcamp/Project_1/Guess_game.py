print('Hi, you want to play a game?...')
a = input('Yes or no?...')
from random import randint

number = randint(1, 100)
counter = 0
print(number)

if a.lower() == 'yes':
    print('Okey!, I am going to think a number and you have to guess it...')
else:
    print('Wrong answer, i am going to think a number, come on guess it...')

guess = int(input('I am ready, what is your first guess...?'))


