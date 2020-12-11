# LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even,
# but returns the greater if one or both numbers are odd

list1 = [0,1, 3, 4]


def lesser_of_two_evens(a,b):
    lst = [a, b]
    while a % 2 == 0 and b % 2 == 0:
        if a < b:
            return a
        else:
            return b
    return max(lst)

print(lesser_of_two_evens(7, 7))

# ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter


def animal_crakers(word):
    word = word.split()
    while len(word) == 2:
        if word[0][0] == word[1][0]:
            return True
        else:
            return False
    return 'Wrong string, please enter a two-word string'

# MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If
# not, return False

def makes_twenty(num1, num2):
    while type(num1) == int and type(num2) == int:
        if num1 == 20 or num2 == 20:
            return True
        elif num1+num2 == 20:
            return True
        else:
            return False
    return 'Please enter integer numbers.'

print(makes_twenty(12, 8))


# OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name

def old_macdonald(name):
    lst = [x for x in name]
    lst[0] = lst[0].upper()
    lst[3] = lst[3].upper()
    name = ''.join(lst)
    return name


print(old_macdonald('macdonald'))


# MASTER YODA: Given a sentence, return a sentence with the words reversed

def master_yoda(sentence):
    sentence = sentence.split()
    sentence = sentence[::-1]
    sentence = ' '.join(sentence)
    return sentence.lower().capitalize()


print(master_yoda('I am home'))


# ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200
def almost_there(n):
    if 90 <= n <= 110 or 190 <= n <= 210:
        return True
    else:
        return False


print(almost_there(204))


# FIND 33:
# Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

s = [1,2,3,4,4]
print(s.count(3))


def find_33(list):
    while list.count(3) >= 2:
        count = 0
        lst=list[0:2]
        if lst == [3, 3]:
            return True
        for number in list:
            count +=1
            lst =list[count:count+2]
            if lst == [3, 3]:
                return True
            else:
                pass
        return False

    return False


print(find_33([3, 1, 3]))


# PAPER DOLL: Given a string, return a string where for every character in the original there are three characters


def paper_doll(stirng):
    str = []
    for letter in stirng:
        str.append(letter*3)
    str = ''.join(str)
    return str


print(paper_doll('hello'))





def paper_doll2(string):
    s = [letter for letter in string]
    order = list(range(len(string)))
    order_s = list(zip(order, s))
    s_final = order_s * 3
    s_final.sort()  # The sort method, sort by the first values of the tuple
    string = [y for x,y in s_final]
    return ''.join(string)


print(paper_doll2('hello'))


# BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. If
# their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment)
# exceeds 21, return 'BUST

def black_jack(a, b, c):
    while 1 <= a <= 11 and 1 <= b <= 11 and 1 <= c <= 11:
        suma = a + b + c
        lst = [a, b, c]
        count = 0
        for element in lst:
            if element == 11 and count < 2 and suma > 21:
                index = lst.index(element)
                lst[index] = 1
                count += 1
            suma = sum(lst)
        if suma > 21:
            return 'BUST'
        else:
            return lst



print(black_jack(3, 11, 11))


one = [1, 2, 3, 4, 5, 6, 9, 7, 5]
two = [2, 3, 5, 6, 7, 8, 9]
three = [3, 5, 6, 7, 9]
four = [7, 7, 8, 6, 9]
five = [3, 5, 6, 4, 9, 3, 1, 4, 6, 5, 9]



def count_69(lst):
    """
    Create a list with the numbers that are between two numbers of a given list. Then we rest the sum of
    the new list to the sum of the original list
    :param lst: Normal list
    :return: the sum of the original list minus the sum f the new list
    """
    add = False
    six_nine = []
    for element in lst:
        while not add:
            if element == 6:
                add = True
                break
            else:
                break
        while add:
            six_nine.append(element)
            if element == 9:
                add = False
                break
            else:
                break


    return sum(lst)-sum(six_nine)


print(count_69(five))


def summer_69(arr):
    total = 0
    add = True

    for num in arr:
        while add:
            if num != 6:
                total += num
                break
            else:
                add = False
        while not add:
            if num != 9:
                break
            else:
                add = True
                break
    return total


print(summer_69(five))


# SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order

def spy_game(lst):
    arr = []
    for element in lst:
        while arr != [0, 0, 7]:
            if len(arr) != 3:
                arr.append(element)
                break
            else:
                arr.pop(0)
                arr.append(element)
                break
    if arr == [0, 0, 7]:
        return True
    else:
        return False


print(spy_game([ 0, 0, 1, 0, 0, 8, 4, 0, 0, 9,5,2]))


# COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to and including a given number

def count_primes(num):
    """
    A prime number it's a number that it's not divisible by any number except the own number
    :param num:
    :return:
    """
    count = 0
    primes = []
    if num <= 2:
        if num == 1:
            return 1
        else:
            return 0
    for element in range(3, num+1):
        for number in range(2, element):
            if element % number == 0:
                break
        else:
            count +=1
            primes.append(element)
    return count



print(count_primes(14))

"""
num = 4

# If given number is greater than 1
if num > 1:

   # Iterate from 2 to n / 2
   for i in range(2, num):

       # If num is divisible by any number between
       # 2 and n / 2, it is not prime
       if (num % i) == 0:
           print(num, "is not a prime number")
           break
   else:
       print(num, "is a prime number")

else:
   print(num, "is not a prime number")

"""


## PRINT BIG: Write a function that takes in a single letter, and returns a 5x5 representation of that letter

def print_big(letter):
    lst = []
    if letter.lower() not in 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.split():
        return 'Please enter a valid letter'
    patterns = {
        1:'* * * * *',
        2: '*        ',
        3: '        *',
        4: '*       *',
        5: '* * * * '
    }
    alphabet = {
        'A':[1,4,4,1,4,4,4],
        'B':[5,4,4,5,4,4,5],
        'C':[1,4,2,2,2,4,1],
        'D':[5,2,2,2,2,2,5],
        'E':[1,2,2,1,2,2,1],
        'F':[1,2,1,2,2,2,2]
    }
    for pattern in alphabet[letter.upper()]:
        print(patterns[pattern])


