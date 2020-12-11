from math import sqrt

# Ternary operator:

a = 4

b = 'a < 5' if a < 5 else 'a > 5'

print(b)


# The ternary opeartor can also be made with any expression

def say_hello():
    print('Hello')


def say_goodbye():
    print('Goodbye')


say_hello() if a < 5 else say_goodbye()


# If we call the function without the parentheses we'll get the object itself

def func_2(a: int, b: int):  # We can specify the type of the parameters "a" and "b", it's a documentation,
    # we can pass any type of parameter
    return a * b


print(func_2)

print(func_2(2, 4))

print(func_2('a', 3))

# The order in which we put de definitions of your function as long as they are not being invoke it doesn't matter


# Lambda function

fn1 = lambda x: x ** 2
print(fn1)

print(fn1(3))

# While loop

# Break statement
print("\nBreak statement")
min_length = 2

name = input("Please enter your name: ")

while not (len(name) >= 2 and name.isprintable() and name.isalpha()):
    name = input("Please enter your name: ")
print("Hello, {0}".format(name))

# It's a good practice to not repeat the code more than once, above e have the input name 2 times, we'd restructure it
# like that

print("\nWhile loop without repeat")
min_length = 2

while True:
    name = input("Please enter your name: ")
    if len(name) >= 2 and name.isprintable() and name.isalpha():
        break
print("Hello, {0}".format(name))

# Continue statement:

"""The continue statement says: In the current iteration that we're in right now, just skip everything that comes 
after that continue statement and go back to the beginning of the loop rerun the test and if it's true continue running
"""
print("\n Continue statement")
a = 0

while a < 10:
    a += 1
    if a % 2 == 0:
        continue
    print(a)

a = 0

while a < 10:
    a += 1
    if a % 2 == 0:
        print(a, ' is odd')
    else:
        continue

# Else statement in while loop:
print("\n\nWhile's else statement")
"""The else clause will only execute if, and only if the while loop didn't encounter a break statement. If the loop 
runs normally
"""

l = [1, 2, 3]
val = 10

# tracking a flag:
print("\n Tracking Flag")
found = False  # flag
idx = 0
while idx < len(l):
    if l[idx] == val:
        found = True
        break
    idx += 1

if not found:
    l.append(val)

print(l)

# Making the same code with else statement, without the flag
print("\nWithout flag, with else")
print("\n\n")
l = [1, 2, 3]
val = 10
idx = 0
while idx < len(l):
    if l[idx] == val:
        break
    idx += 1
else:
    l.append(val)

print(l)

# try...except...finally (that last one always run)
print("\nTry and expect")
a = 10
b = 0

try:
    a / b
except ZeroDivisionError:
    print('Division by 0')
finally:
    print('This always execute')


print("\n\n While loop with a continue statement")
a = 0
b = 2
while a < 4:
    print('----------')
    a += 1
    b -= 1

    try:
        a / b
    except ZeroDivisionError:
        print("{0}, {1} - Division by 0".format(a, b))
        continue
    finally:
        print("{0}, {1} - always execute".format(a, b))  # This will always execute

    print("{0}, {1} - main loop".format(a, b))  # This won't execute if we reach the exception


print("\n\nWhile loop with break and else statement")
a = 0
b = 10
while a < 4:
    print('----------')
    a += 1
    b -= 1

    try:
        a / b
    except ZeroDivisionError:
        print("{0}, {1} - Division by 0".format(a, b))
        break
    finally:
        print("{0}, {1} - always execute".format(a, b))  # This will always execute

    print("{0}, {1} - main loop".format(a, b))  # This won't execute if we reach the exception
else:
    print('Code executed without a ZeroDivisionError')


# FOR loops.

# What's an iterable? In Python, an iterable is an object capable of returning values one at a time.

# FOR loop in other c* languages

# for (int i=0; i <5; i++) {...piece of block...}
# We can rewrite this in python as a while loop
print('\n\nFor loop')
i = 0
while i < 5:
    print(i)
    i += 1
i = None  # In those laguages the variable dissapears with the fpr statement

for i in range(5): #range it's an iterable
    print(i)

for i in [1, 2, 3, 4, 5]:
    print(i)


for x in 'hello':
    print(x)


for x in [(1, 2), (3, 4), (5, 6)]:
    print(x)

for i,j in [(1, 2), (3, 4), (5, 6)]:
    print(i,j)


# we can use continue, break and else statement
print('\n\nFor loop with break and else')
for i in range(1,8):
    print(i)
    if i % 7 == 0:
        print('Multiple of 7')
        break
else:
    print('No multiple of 7 in this range')


print('\n\nFor loop with try and except')

for i in range(5):
    print('----------------------------')
    try:
        10 / (i-3)
    except ZeroDivisionError:
        print('Divided by 0')
        continue
    finally:
        print('Always run')


    print(i)

print('\nFor loop with counter for track the index')
s = 'hello'
i = 0
for c in s:
    print(i, c)
    i += 1

print('\n\nFor loop using string indexes')
for i in range(len(s)):
    print(i, s[i])

print('\n\nFor loop using enumerate function')

s='hello'
for i, c in enumerate(s):  # The enumerate, enumerates an iterable that has indexes, and returns the index and the
    # element in a tuple
    print(i, c)


