# Some strings are also automatically interned BUT NOT ALL!

# As Python code is compiled, identifiers are interned
# Variable names
# Function names
# Class names
# ...
# Identifiers should start with an underscore "_" or a letter. And can only contain letters, underscores and numbers

# Some strings may also be automatically interned.
# Strings literals that look like identifiers: 'hello_world'
# Although it starts with a digit, even thought that is not a valid identifier it may still get interned.

# ALL ABOUT OPTIMIZATION: SPEED AND MEMORY

# Python deals with a lot of dictionaries type lookups on string keys, ehich means a lot of equality testing.

a = 'some_long_string'
b = 'some_long_string'

# If we want to compare a == b --> we'll compare character by character
# If we know that 'some_long_string' has been interned then 'a' and 'b' are the same string if they both point to the
# same memory address.
# In which case we can use "a is b" instead. Which compares two integers (memory addresses)

# We can force strings to be interned by using the "sys.intern() method.

# ¿ When we should use it ?
# Dealing with large number of string that could have high repetition: tokenizing a large corpus of text (NLP)
# Lots of string comparision

a = 'hello'
b = 'hello'


def references(a, b):
    if a is b:
        print("The sting IS INTERNED and share the memory address\n'a' address: {0}\n'b' address: "
              "{1}".format(id(a), id(b)))
    else:
        print("The string is NOT INTERNED.\n'a' address: {0}\n'b' address: {1}".format(id(a), id(b)))


def share_address(a, b):
    if a is b and a == b:
        print("They both have the same address and the same state.\nAddress: {0}, 'a is b': {1}\nState: {2}, "
              "'a == b': {3}".format(id(a), (a is b), a, (a == b)))
    if a is not b and a == b:
        print("They both share State: \n{0}, 'a == b': {1}. But they don't share address, 'a is b': {2}.\n'a' "
              "address: {3}\n'b' address: {4}".format(a, (a is b), (a == b), id(a), id(b)))


print('Both string have HELLO')
references(a, b)
print("")
# As the memory address is interned the address and the state will be the same for those who have the string interned.
share_address(a, b)
print("")

print("Both string have hello world")
a = 'hello world'
b = 'hello world'
references(a, b)
print("")
share_address(a, b)
print("")

print("\nReally long string: ")
a = "My name is Alex Abades Grimes and I am 25 years old" * 200
b = "My name is Alex Abades Grimes and I am 25 years old" * 200

references(a, b)
share_address(a, b)

# In the case that the addresses of the strings are different, and you want to intern them:

import sys

a = sys.intern('hello world')
b = sys.intern('hello world')
c = 'hello world'


# Once you try to intern a string by your own, as above, you must intern all the instances of that string


def comparing_using_equals(n):
    a = "My name is Alex Abades Grimes and I am 25 years old" * 200
    b = "My name is Alex Abades Grimes and I am 25 years old" * 200
    for i in range(n):
        if a == b:
            pass


def compare_using_interning(n):
    a = sys.intern("My name is Alex Abades Grimes and I am 25 years old" * 200)
    b = sys.intern("My name is Alex Abades Grimes and I am 25 years old" * 200)
    for i in range(n):
        if a is b:
            pass


import time
import pandas as pd

time_matx = pd.DataFrame(data=None, index=range(10), columns=['time_equals', 'time inter'])
print(time_matx)
print("")
print(time_matx.shape[0])
print(time_matx['time_equals'][1])


for i in range(time_matx.shape[0]):
    # Using the equal comparision ==
    start = time.perf_counter()
    comparing_using_equals(10000000)
    end = time.perf_counter()
    lapse_time = end - start
    time_matx['time_equals'][i] = lapse_time

    # Using the intern comparision
    start = time.perf_counter()
    compare_using_interning(10000000)
    end = time.perf_counter()
    time_lapse = end - start
    time_matx['time inter'][i] = time_lapse


import matplotlib.pyplot as plt

print(time_matx)
plt.figure()
time_matx.plot()
plt.show()



