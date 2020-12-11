print('hello world %s I am studying' % 'motherfucker')
print("Hello, I'm a very %r student" % '\tstubborn')
print("Ok it seems %s this is to %s" % ('that', '\teasy'))
print("Ok the number is: %12.5f" % (13.4))
print("A %s saved is a %s earned" % ('penny', 'penny'))
print("A {} saved is a {} earned".format('penny', 'penny'))
print("A {p} saved is a {p} earned".format(p='penny'))

print('{0:8} | {1:>20}'.format('Fruit', 'Quantity'))
print('{0:8} | {1:9}'.format('Apples', 3.))
print('{0:8} | {1:9}'.format('Oranges', 10))

print("{0:=<10} | {1:-^10} | {2:.>10}".format('Left', 'Center', 'Right'))

print('This is my ten-character, two-decimal number:%15.4f' % 13.579)
print('This is my ten-character, two-decimal number:{0:15.4f}'.format(13.579))

name = 'Alex'
print(f'He said his name is {name}')
print(f'He said his name was {name!r}')

#### Float formatting follows `"result: {value:{width}.{precision}}"`
num = 23.45678
print(f"My 10 character, four decimal number is:{num:{15}.{5}}")
print(f"My 10 character, four decimal number is:{num:{15}.{7}}")
## Note that with f-strings, precision refers to the total number of digits, not just those following the decimal.

print(f"My 10 character, four decimal number is:{num:15.7f}")

my_dict = {
    'key1': 123,
    'key2': [12, 23, 33],
    'key3': ['item0', 'item1', 'item2']
}
print('\n')
my_dict['key2'][0] -= 2
print(my_dict['key2'][0])
my_dict['key3'] = 'Wallapopp'
print(my_dict['key3'])

d = [index for index in my_dict['key2']]
print(d)

new_dict = {}

new_dict['hel'], new_dict['Best'], new_dict['astro'] = ('Is cool', [23, 34, 31], ('hell', 56, True))
print(new_dict)
new_dict['astro'] = 34
print(new_dict)

d = {'key1': {'key2': {'key3': 'Hurray'}}}
print(d['key1']['key2']['key3'])
print(d.keys())

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())

t = ('hello', 54, True, 'hello', False, 4, 42, 'pip')
print(t.index(False))
print(t.count(int))  ## We can count the number that a string appears or a float or specific type of an object

list1 = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]
print(list1)
list1 = set(list1)
print(list1)

# Create a txt and write inside
openfile = open('Probe.txt', 'w')
openfile.write('Hello this is a quick test file')
openfile.close()

# Checking the path file

import os

print(os.getcwd())
print('\n')
print(os.listdir())  # Can We get the path of a specific file?

from pathlib2 import PureWindowsPath

print(PureWindowsPath('Probe.txt'))

my_file = open('Probe.txt')
print(my_file.read())
# Once we read it we have to reset the index

my_file.seek(0)
print(my_file.read())

my_file.seek(0)
my_file.close()
print('\n')

my_file = open('Probe.txt', 'w+')
my_file.write('Hello, this is a new line')
my_file.seek(0)
print(my_file.read())
my_file.close()

my_file = open('Probe.txt', 'a+')
my_file.write("\nSo this it's going to be a new line")
my_file.write("\nAnd we can write another line too")
my_file.write("\nWe can try to write two new lines with\nthis method, so we don't have to constantly\nwrite and "
              "writhe the object name and the method")
my_file.close()

for line in open('Probe.txt'):
    print(line)

import numpy as np

np.sqrt

list2 = np.zeros((1, 3))

print(list2)

tup = ((1, 2), (3, 4), (5, 6), (7, 8))

for t1, t2 in tup:
    print(t1)
    print(t2)

x = 0
while x != 10:
    print('x it is currently: ', x)
    x += 1
    if x == 8:
        print('Breaking because x it is equal to: ', x)
        break
    else:
        print('Continuing...')
        continue

list3 = list(range(0,11))
print(list3)

index_count = 0

for index in 'abcde':
    print('At index {} the letter is {}'.format(index_count, index))
    index_count+=1

print('\nAnother way to do it it is: '
       '\n')

for i, letter in enumerate('abcde'):
    print('At index {} the letter is {}'.format(i, letter))

print('\n')
list4= list(enumerate('abcde'))
print(list4)

list5 = 'a b c d e f g h i j'.split()

print(list5)
tuplelist= list(zip(list3, list5))
print(tuplelist)

for item1, item2 in zip(list3, list5):
    print('The first item it is {} and the second item it is {}'.format(item1, item2))

print('x' in ['x', 'y', 'z'])

print('x' not in ['x', 'y', 'z'])

list6 = list(range(0, 21))
print(list6)

from random import shuffle

shuffle(list6)
print(list6)
print('\n')

## LIST COMPREHENSIONS

lst = [x for x in 'abcde']
print(lst)

lst2 = [pow(x,2) for x in range(0,11)]
print(lst2)

from random import randint

print(randint(0,101))

lst3 = [x for x in range(0,11) if x%2==0]
print(lst3)

celsius = [0,10,20.1,34.5]

fahrenheit = [((9/5)*temp+32) for temp in celsius]
print(fahrenheit)

lst = [ x**2 for x in [x**2 for x in range(11)]]
print(lst)

st = 'Print only the words that start with s in this sentence'


for word in st.split():
    if word[0]=='s':
        print(word)


for number in range(11):
    if number%2==0:
        print(number)

lst=list(range(0,11,2))
print(lst)

lst = [x for x in range(51) if x%3==0]
print(lst)

st = 'Print every word in this sentence that has an even number of letters'

lst = [x for x in st.split() if len(x)%2==0]
print(lst)

# # Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the
# number, and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print
# "FizzBuzz".

for number in range(101):
    if number%3==0:
        print('Fizz')
    elif number%5==0:
        print('Buzz')
    elif number%3==0 and number%3==0:
        print('FizzBuzz')
    else:
        print(number)

## Use List Comprehension to create a list of the first letters of every word in the string below:
st = 'Create a list of the first letters of every word in this string'

lst = [x[0] for x in st.split()]
print(lst)