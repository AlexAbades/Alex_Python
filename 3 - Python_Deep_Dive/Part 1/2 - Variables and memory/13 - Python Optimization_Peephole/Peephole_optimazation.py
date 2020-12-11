# Peephole optimization. --> it runs with our code, so it's compiled at the same time that our code.
# If we close the file and rerun it it eill recompile again. In other languages that goes different

# For some reasons, readability reasons we may want to et our code as a multiplication.
# For example. If our line of code makes a calculation of the minutes of a day, it's easier to understand a line of code
# that has 24 * 60 than 1440. The coder, or other readers, will know where that number comes from.

# If we repeat that expression a lot on our code (24 * 60) we may think that it's a better choice to put than as a
# constant for speed or time optimization. But Python does that for us. It will convert that 'constant' expression into
# a constant and instead of do the expression, it will read 1440.

# It happens with short sequences < 20
# (1, 2) * 5 --> (1, 2, 1, 2, 1, 2, 1, 2, 1, 2)
# 'abc' * 3 --> 'abcabcabc'
# 'hello' + 'world' --> 'hello world'

# It won't do it with:
# 'the quick brown fox' * 10 (more than 20 char)

# Trade off between storage and computation. It does it at 20 char.

# MEMBERSHIPS TEST: Mutable are replaced by immutable

# IF e IN [1, 2, 3]:
# Even that the list is mutable, while our code is running, that list is not going to change in that specific context
# so it's a constant, and replaced by its immutable counterpart --> Tuple (1, 2, 3)
# Lists --> tuples
# sets --> frozensets

# Set is much faster than list or tuple membership (because sets are basically dictionaries)

# Instead of writing: IF e IN [1, 2, 3]: or IF e IN (1, 2, 3):
# write: IF e IN {1, 2, 3}:

def my_func():
    a = 24 * 60
    b = (1, 2) * 5
    c = 'abc' * 3
    d = 'ab' * 11  # More than 20 char
    e = 'the quick brown fox' * 5
    f = ['a', 'b'] * 3


# Take a look to the constants, we can see those who have less than 20 char

print(my_func.__code__.co_consts)


def my_func(e):
    if e in [1, 2, 3]:
        pass


print(my_func.__code__.co_consts)
# Take a look to the constants in the func. The list has become a tuple.


def my_func(e):
    if e in {1, 2, 3}:
        pass


print(my_func.__code__.co_consts)
# Take a look to the constants in the func. The set has become a frozenset.

import string
import time

print(string.ascii_letters)

char_list = list(string.ascii_letters)
char_tuple =  tuple(string.ascii_letters)
# They both, list and tuples are ordered sequences
print("\nAscii string")
char_set = set(string.ascii_letters)
print("\nList of the Ascii string")
print(char_list)
print("\nTuple of the Ascii string")
print(char_tuple)
print("\nSet of the Ascii string")
print(char_set)


def membership_test(n, container):
    for i in range(n):
        if 'z' in container:
            pass


start = time.perf_counter()
membership_test(10000000, char_list)
end = time.perf_counter()
lst_lapse = end - start

start = time.perf_counter()
membership_test(10000000, char_tuple)
end = time.perf_counter()
tpl_lapse = end - start

start = time.perf_counter()
membership_test(10000000, char_set)
end = time.perf_counter()
set_lapse = end - start

print("The time it took to run 10 million times for the different containers is: ")
print("List: {0}, average {1}".format(lst_lapse, lst_lapse/10000000))
print("Tuple: {0}, average {1}".format(tpl_lapse, tpl_lapse/10000000))
print("Set: {0}, average {1}".format(set_lapse, set_lapse/10000000))
