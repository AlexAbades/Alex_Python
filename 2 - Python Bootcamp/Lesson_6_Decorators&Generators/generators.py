

def create_cubes(n):
    cubes = []
    for x in range(n):
        cubes.append(x**3)
    return cubes


print(create_cubes(10),'\n')

# We are holding the list in memory. That is not a problem if we want the actual list, but in the most cases,
# what we want is to print an element

for x in create_cubes(10):
    print(x)

# Instead of creating a list, which takes up memory, we can create a function which yields the number
# until the next number arrives

print('\n')


def create_cubes(n):
    for number in range(n):
        yield number**3


for x in create_cubes(10):
    print(x)


def get_fibo(n):

    a = 1
    b = 1
    for item in range(n):  # 0, 1, 2, 3, 4, 5, 6, 7
        yield a
        a, b = b, a+b
        # 1, 1 = 1, 1+1
        

print('\nFibbo:')
for x in get_fibo(10):
    print(x)


print('\n\n')



def simple_func():
    for x in range(3):
        yield x


for number in simple_func():
    print(number)


# The generator only yields or storage the last item result of a function

g = simple_func()
print(g)
# We can call the items that are yield in the generator
print(next(g))
print(next(g))
print(next(g))
try:
    print(next(g))
except StopIteration:
    print('# If we call more times the the next function, which calls the yield item, StopIteration')

# If we call more times the the next function, which calls the yield item,
# we'll get the StopIteration error. In the for loop, what's really asking is for the next item until
# this error appears.



# ITER FUNCTION
# It allows us to actually iterate through a normal object that we may not expect
# For example: A string is an iterable object iterable, but it doesn't mean that the string itself it's going to
# be able to iterate with the next function, because does not support the generator, so they aren't an iterator
print('\nIter function')
s = 'Hello'

for letter in s:
    print(letter)

try:
    print(next(s))

except TypeError:
    print("TypeError: 'str' object is not an iterator")


# In order to convert the string into a generator, we have to call the iter function
print('\ns iterator:\n')
s_iter = iter(s)

print(next(s_iter))
print(next(s_iter))

# We convert an object that are iterable into iterators

# Exercises
print('\n\nExercises:')

# Create a generator that generates the squares of numbers up to some number N.


def gen_squares(n):
    for num in range(n):
        yield num**2


for x in gen_squares(10):
    print(x)


# Create a generator that yields "n" random numbers between a low and high number (that are inputs).
print('\n\n')
from random import randint


def rand_numbers(low, high, n):
    for x in range(n):
        yield randint(low, high)


for x in rand_numbers(1, 10, 12):
    print(x)

print('\n')
s = 'Spaghetti'
s_iter = iter(s)
print(next(s_iter))

# GENERATOR EXPRESSIONS
# It's very similar to list comprehension, but instead of using squarebraquets, we use parentheses

print('\nComprehension: ')
my_comp = [x**2 for x in range(20) if x % 2 == 0]
print('We create a list: ')
print(my_comp)
print('')

my_gene = (x**2 for x in range(20) if x % 2 == 0)
print('We create a generator')
print(my_gene)
print(next(my_gene))
print(next(my_gene))
print('')

for x in my_gene:
    print(x)

# The advantages are the storage in memory
print('\n\n')
from sys import getsizeof

my_comp = [x**5 for x in range(1000)]
print('List:')
print(my_comp)
print('Memory storage: ', getsizeof(my_comp))
print('')

my_gene = (x**5 for x in range(1000))
print('Generator')
print(my_gene)
print('Memory storage: ', getsizeof(my_gene))


