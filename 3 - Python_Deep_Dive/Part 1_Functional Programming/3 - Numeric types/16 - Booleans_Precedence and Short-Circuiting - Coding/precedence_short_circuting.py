# Boolean operators

# TRUTH TABLE
#  X--Y  | NOT X | X AND Y | X OR Y
#  0  0  |   1   |    0    |   0
#  0  1  |   1   |    0    |   1
#  1  0  |   0   |    0    |   1
#  1  1  |   0   |    0    |   1

# COMMUTATIVITY
# A or B == B or A
# A and B == B and A

# DISTRIBUTIVITY
# A and (B or C) == (A and B) or (A and C)
# A or (B and C) == (A or B) and (A or C)

# Associativity
# A or (B or C) == (A or B) or C  --> A or B or C
# A and (B and C) == (A and B) and C --> A and B and C
# Python will choose to go left to right for evaluation.

# De Morgan's Theorem
# not(A or B) == (not A) or (not B)
# not(A and B) == (not A) and (not B)

# MISCELLANEOUS
# not(x < y) == x >= y
# not(x <= y) == x > y
# not(x > y) == x <= y
# not(x >= y) == x < y


# OPERATOR PRECEDENCE (descending order)
# ()
# <, >, <=, >=, ==, !=, in, is
# not
# and
# or

# True or True and False
#         |and  first --> False
# True or False
# True

# SHORT-CIRCUIT EVALUATION

# OR operator: always a True value when X is True
# If X is True, then (X or Y) will be True no matter the value of Y
# (X or Y) will return True without evaluating Y if X is True

# AND operator: always a False value when X is False
# If X is False, then (X and Y) will be False no matter the value of Y
# (X and Y) will return False without evaluating Y if X is False.

# and operates first
print(True or True and False)
print(True or (True and False))

# or operates first
print((True or True) and False)
print("")

# Short Circuiting
a = 10
b = 3


def twice(a, b):
    if a / b > 2:
        print("A IS AT LEAST TWICE THAN B")


twice(a, b)

# but what happens if b is 0?
b = 0


# twice(a, b)
# ZeroDivisionError: division by 0


# We could define a nested if statement for that

def twice_if(a, b):
    if b > 0:
        if a / b > 2:
            print("A IS AT LEAST TWICE THAN B")


print("If statement")
twice_if(a, b)
b = 3
twice_if(a, b)


def twice_if_line(a, b):
    if b > 0 and a / b > 2:
        print("A IS AT LEAST TWICE THAN B")


def twice_truthy(a, b):
    if b and a / b > 2:
        print("A IS AT LEAST TWICE THAN B")


import time


def twice_if(a, b, n_iter):
    for i in range(n_iter):
        if b > 0:
            if a / b > 2:
                pass


def twice_if_line(a, b, n_iter):
    for i in range(n_iter):
        if b > 0 and a / b > 2:
            pass


def twice_truthy(a, b, n_iter):
    for i in range(n_iter):
        if b and a / b > 2:
            pass


times_list = []


def get_time(function):
    a = 10
    b = 3
    n_iter = 10000000
    start = time.perf_counter()
    function(a, b, n_iter)
    end = time.perf_counter()
    lapse = end - start
    times_list.append(lapse)



get_time(twice_if)
get_time(twice_if_line)
get_time(twice_truthy)


print("The nested if statement takes: {0}".format(times_list[0]))
print("The one line double if statement takes: {0}".format(times_list[1]))
print("The truthy and if statement takes:  {0}".format(times_list[2]))


import string

name = 'Bob'

if name[0] in string.digits:
    print('Name cannot start with a digit')

name = ''

if len(name) > 0 and name[0] in string.digits:
    print('Name cannot start with a digit')
# Works well for empty strings but not for None values

name = None
if name is not None and len(name) > 0 and name[0] in string.digits:
    print('Name cannot start with a digit')
# Works well for every situation, None values, empty string, normal strings
# We can see the truthyness of the object

# Sequence types will return the length when we look at the truthyness
name = 'abd'
name1 = ''
print("")
print(name)
print("")
print(name1)
print("")
print(name.__len__())
print(name1.__len__())
print(bool(name.__len__()))
print(bool(name1.__len__()))

if name and name[0] in string.digits:
    print('Name cannot start with a digit')