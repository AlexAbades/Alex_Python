# TRUTH VALUES

# Every object has a True truth value, except.
# None
# False
# 0 in any numeric type (0, 0.0, 0+0j)
# Empty sequences (e.g. list, tuple, string...)
# Empty mapping types (e,g, dictionary, set,...)
# Custom classes that implement a __bool__ or __len__ method that returns False or 0


# Classes define their truth values by defining a special instance method:
# __bool __ or (__len__)

# when we call bool(x) --> Python is actually executing x.__bol__()
# If it doesn't find __bool__ (doesn't defined) tries to execute __len__ if neither is defined, then return True
# (is the default). Returns True unless one of the above methods returns False

# INTEGERS

# def __bool__(self):
#      return self != 0
# when we execute bool(100) --> 100.__bool__() --> 100 != 0 --> True
# when we execute bool(0) --> 0.__bool__() --> 0 != 0 --> False
print("Integers:")
print(bool(5))
print(bool(0))
print(bool(0.0))
print(bool(0 + 0j))
print(bool(-4))

from fractions import Fraction
from decimal import Decimal
print("\nFracion and Decimal")
print(bool(Fraction(0, 1)))
print(bool(Decimal('0.0')))

# SEQUENCES
# Sequence [1, 2, 3] --> it will look at the len method, as the list len is 3 it will return False
lst = [1, 2, 3]
print(lst)
# bool(lst)--> lst.__len__() --> len(lst) if len(lst)>0 True
print('\nSequences:')
print(bool(lst))
print(bool([]))
a = []
print(a)
print(type(a))
print("\nEmpty list")
print(bool(a))
# What we are doing, getting the len, and then passing in into the boolean
print(a.__len__())
print(bool(a.__len__()))

# if my_list:
#    block code: it will execute if and only if my_list is both not None and not empty
# Equivalence:
# if my_list in not None and len(my_list) > 0:
#    block code

# Why are they equivalent?
# The first expression has an object inside a if statement.
# The if statement Python knows needs to be a boolean result, so it's going to look at the truthyness of my_list,
# if the truthyness evaluates to True it would execute the code, if not, no.

# STRINGS
print("\nStrings:")
print(bool('abc'))
print(bool(''))

# TUPLES
print("\nTuples")
a = (1, 2)
b = ()
print(a, type(a))
print(b, type(b))
print("Boolean values")
print(bool(a))
print(bool(b))
print("Length values")
print(a.__len__())
print(b.__len__())
print("Evaluating the length to 0")
print(bool(a.__len__()))
print(bool(b.__len__()))

# MAPPING STRUCTURES
print("\nDictionaries and sets:")
a = {}  # dictionary
b = set()
print(a, type(a))
print(b, type(b))
print("Boolean values:")
print(bool(a))
print(bool(b))
print("Length values:")
print(a.__len__())
print(b.__len__())
print("Evaluating the length to 0 (slef != 0):")
print(bool(a.__len__()))
print(bool(b.__len__()))

print("\nDictionaries and sets:")
a = {'a': 2, 'b': 3}  # dictionary
b = {1, 2, 4}
print(a, type(a))
print(b, type(b))
print("Boolean values:")
print(bool(a))
print(bool(b))
print("Length values:")
print(a.__len__())
print(b.__len__())
print("Evaluating the length to 0 (slef != 0):")
print(bool(a.__len__()))
print(bool(b.__len__()))
# print(help(list))


# NONE OBJECT
print("")
print(bool(None))
# Always evaluates to False, it allows to use it in if statement
# In python, if we have a boolean expression we can actually put object instead a boolean value. Python will detect
# that's an object and will evaluate the object to its truthyness (truth value)

print("\nObject evaluating in if statement")
a = [1, 2, 3]

if a is not None and len(a) > 0:
        print(a[0])
else:
    print('Nothing to see here...')

if a:  # --> will evaluate for us bool(a)
    print(a[0])
else:
    print('Nothing to see here...')

print("")
a = []

if a is not None and len(a) > 0:
        print(a[0])
else:
    print('Nothing to see here...')

if a:  # --> will evaluate for us bool(a)
    print(a[0])
else:
    print('Nothing to see here...')

print("\nChanging the order of the long expression empty list")
a = [1, 2, 3]

if len(a) > 0 and a is not None:
        print(a[0])
else:
    print('Nothing to see here...')

if a:  # --> will evaluate for us bool(a)
    print(a[0])
else:
    print('Nothing to see here...')

# If the list has an element, it won't throw an error, 'cause first is evaluating the len, as it has len, will
# pass tto the second boolean expression is not None

# But What happens if the list is assigned to None?
print("Empty list len evaluation first")
a = None

if len(a) > 0 and a is not None:
        print(a[0])
else:
    print('Nothing to see here...')

if a:  # --> will evaluate for us bool(a)
    print(a[0])
else:
    print('Nothing to see here...')

# The None object has no len, that's why we get an error

a = None

if a is not None and len(a) > 0:
        print(a[0])
else:
    print('Nothing to see here...')

if a:  # --> will evaluate for us bool(a)
    print(a[0])
else:
    print('Nothing to see here...')

# It will evaluate, because first will evaluate the is None boleean, as it recive a False, it wont be necessary to
# evaluate anything more.
