# Write a function that computes the volume of a sphere given its radius

import numpy as np

print('Ex 1:')


def volume(r):
    if r>0:
        return 4/3*np.pi*r**3
    else:
        return 'Invalid radius'


print(volume(2))





# Write a function that checks whether a number is in a given range (inclusive of high and low)

print('\n\n\n')
print('Ex 2:')


def ran_check(num, low, high):
    if low<num<high:
        print(num, 'is in the range between ', low, ' and ', high)
    elif low == num or high == num:
        print(num, "it's not in the range, but it's the bounder!")
    else:
        pass


ran_check(2,2,9)


print('\n\n\n')
print('Ex 2.1:')

def ran_check(num, low, high):
    if num in range(low, high+1):
        print('{} is in range between {} and {}'.format(num, low, high))


ran_check(2,2,9)


print('\n\n\n')
print('Ex 3:')

def myfunc(*args):
    lst = []
    for element in args:
        if element % 2 == 0:
            lst.append(element)
        else:
            pass
    return lst

print(myfunc(2,3,4,5,6))


print('\n\n\n')
print('Ex 4')


def myfunc(string):
    count = 1
    lst = []
    for element in string:
        if count % 2 == 0:
            lst.append(element.upper())
        else:
            lst.append(element.lower())
        count +=1
    return ''.join(lst)

print(myfunc('Anthropomorphism'))



# Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters
print('\n\n\n')
print('Ex 5')

def myfunc(string):
    up = 0
    lw = 0
    for element in string:
        if element.isupper():
            up += 1
        elif element.islower():
            lw += 1
        else:
            pass
    print(f"It has {up} upper cases and {lw} lower cases")


myfunc('Hello Mr. Rogers, how are you this fine Tuesday?')


print('\n\n\n')
print('Ex 5.1')

def myfunc(string):
    d = {'up': 0, 'lw': 0}
    for c in string:
        if c.isupper():
            d['up'] += 1
        elif c.islower():
            d['lw'] += 1
        else:
            pass
    return f"We have {d['up']} upper and {d['lw']} lower"


print(myfunc('Hello Mr. Rogers, how are you this fine Tuesday?'))


# Write a Python function that takes a list and returns a new list with unique elements of the first list.
print('\n\n\n')
print('Ex 6')


def myfunc(lst):
    return list(set(lst))


print(myfunc([1,1,1,1,2,2,3,3,3,3,4,5]))


# Write a Python function to multiply all the numbers in a list.
print('\n\n\n')
print('Ex 7')

def myfunc(lst):
    value = 1
    for element in lst:
        value = value*element
    return value


print(myfunc([1, 2, 3, -4]))


print('\n\n\n')
print('Ex 7.1')

def myfunc(lst):
    value = 1
    for element in lst:
        value *= element
    return value


print(myfunc([1, 2, 3, -4]))


# Write a Python function that checks whether a word or phrase is palindrome or not.
print('\n\n\n')
print('Ex 8')

def palin(string):
    if string.replace(' ','') == string[::-1].replace(' ',''):
        return True
    else:
        return False


print(palin('nurses run'))

print('\n\n\n')
print('Ex 8.1')


def palin(string):
    string = string.replace(' ', '')
    return string == string[::-1]


print(palin('nurses run'))



# # Write a Python function to check whether a string is pangram or not. (Assume the string passed in does not have
# any punctuation)
# Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
# For example : "The quick brown fox jumps over the lazy dog"
print('\n\n\n')
print('Ex 9')

import string

"""
    ascii_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
    ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digits = '0123456789'
    hexdigits = '0123456789abcdefABCDEF'
    octdigits = '01234567'
    printable = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c'
    punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    whitespace = ' \t\n\r\x0b\x0c'
"""
# alphabet = string.ascii_lowercase

def panagram(str, alphabet = string.ascii_lowercase):

    str = str.replace(' ', '').lower()
    str = sorted(list(set(str)))
    str = ''.join(str)

    if str == alphabet:
        return  "It's a panagram"
    else:
        return "It's not a panagram..."


print(panagram('The quick brown fox jumps over the lazy dog'))



# We can compare sets, look at that link
# https://medium.com/better-programming/a-visual-guide-to-set-comparisons-in-python-6ab7edb9ec41

print('\n\n\n')
print('Ex 9.1')


def panagram(str, alphabet = string.ascii_lowercase):


    if str == alphabet:
        return  "It's a panagram"
    else:
        return "It's not a panagram..."


print(panagram('The quick brown fox jumps over the lazy dog'))