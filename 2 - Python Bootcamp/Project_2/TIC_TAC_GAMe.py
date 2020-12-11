from random import randint

print('Table')

print('  1    2    3 ')
print('    |    |    ', 'A')
print('----|----|----')
print('    |    |    ', 'B')
print('----|----|----')
print('    |    |    ', 'C')

print('\n')
print('Comptuer nomenclature')

print('  1 |  2 |  3 ')
print('----|----|----')
print('  4 |  5 |  6 ')
print('----|----|----')
print(' 7  |  8 |  9 ')

"""

winner combinations:

1. A1 + A2 + A3
2. B1 + B2 + B3
3. C1 + C2 + C3
4. A1 + B1 + C1 
5. A1 + B2 + C3 
6. A3 + B3 + C3
7. A1 + B2 + C3
8. A3 + B2 + C1 

"""

# Global variable for assign the moves, it's a dictionary that contains the movements
p_k = {
    'a1': ' ',
    'a2': ' ',
    'a3': ' ',
    'b1': ' ',
    'b2': ' ',
    'b3': ' ',
    'c1': ' ',
    'c2': ' ',
    'c3': ' '
}

# All the winner combinations
win_comb = {
    'comb1': ['a1', 'a2', 'a3'],
    'comb2': ['b1', 'b2', 'b3'],
    'comb3': ['c1', 'c2', 'c3'],
    'comb4': ['a1', 'b1', 'c1'],
    'comb5': ['a2', 'b2', 'c2'],
    'comb6': ['a3', 'b3', 'c3'],
    'comb7': ['a1', 'b2', 'c3'],
    'comb8': ['a3', 'b2', 'c1']

}


# Function that asks to the user their move and returns one of the possible movments
def user_in():

    # Parameters
    global p_k
    choice1 = 'wrong'
    choice2 = 'wrong'
    lst = ['A', 'B', 'C']
    ran = False

    # Select the row
    while choice1.upper() not in lst:
        choice1 = input('Please select a row. Choose between A, B or C:   ').upper()

        if not choice1.isalpha():
            print("Hey, that's not even a letter!")
        elif choice1 in lst:
            pass
        else:
            print("Okei, we are getting closer, but there isn't this row in the table!")

    # Select the column
    while not choice2.isdigit() or not ran:
        choice2 = input('Now you have to select a column! 1, 2 or 3:   ')

        if not choice2.isdigit():
            print("Hey that's not even a number!")

        if choice2.isdigit():
            if int(choice2) not in range(1, 4):
                print('Wrong!!! out of range')
                ran = False
            else:
                ran = True
    final_choice = choice1.lower() + str(choice2)
    p_k[final_choice] = 'X'


# Function that display the Tic Toc table
def display():

    # Variables
    global p_k
    a = "{0:^3} | {1:^3}|{2:^3}  A".format(p_k['a1'], p_k['a2'], p_k['a3'])
    b = "{0:^3} | {1:^3}|{2:^3}  B".format(p_k['b1'], p_k['b2'], p_k['b3'])
    c = "{0:^3} | {1:^3}|{2:^3}  C".format(p_k['c1'], p_k['c2'], p_k['c3'])
    r = "----|----|----"
    col = "{0:^3}   {1:^3}  {2:^3}".format(1, 2, 3)

    # Display
    print(col)
    print(a)
    print(r)
    print(b)
    print(r)
    print(c)


# Function that checks if there is a player winner combination with more than two pieces
def check_player_win_comb():
    """
    Function that checks all the winner combinations and return the first of that combinations that have more than two
    pieces from the player.
    :return: The combination that has two pieces of the player
    """
    count = 0
    win = []
    for comb in win_comb:
        for el in win_comb[comb]:
            win.append(p_k[el])
            # count += 1

        win = ''.join(win).replace(' ', '')
        count += 1
        if win == 'XX':
            break
        else:
            win = []
    else:
        count = 0
    final_combination = 'comb'+ str(count)
    return final_combination


def check_comp_win_comb():
    """
    Function that checks all the winner combinations and return the first of that combinations that have more than two
    pieces from the computer.
    :return: combination with two pieces from computer
    """
    count = 0
    win = []
    for comb in win_comb:
        for el in win_comb[comb]:
            win.append(p_k[el])
            # count += 1

        win = ''.join(win).replace(' ', '')
        count += 1
        if win == 'OO':
            break
        else:
            win = []
    else:
        count = 0
    final_combination = 'comb'+ str(count)
    return final_combination











def check_player_win_comb():
    """
    Function that checks all the winner combinations and return the first of that combinations that have more than two
    piece, it doesn't difference if it's a player piece or a computer piece
    :return: The cunter
    """
    global win_comb
    count = 0
    win = []
    for comb in win_comb:
        for el in win_comb[comb]:
            win.append(p_k[el])

        win = ''.join(win).replace(' ', '')
        count += 1
        if win == 'XX':
            break
        else:
            win = []
    else:
        count = 0

    return 'comb' + str(count)

check_player_win_comb()

def computer_choice():
    global win_comb
    com_dic = {
        1: 'a1',
        2: 'a2',
        3: 'a3',
        4: 'b1',
        5: 'b2',
        6: 'b3',
        7: 'c1',
        8: 'c2',
        9: 'c3'
    }



print('computer choice: ',computer_choice())















