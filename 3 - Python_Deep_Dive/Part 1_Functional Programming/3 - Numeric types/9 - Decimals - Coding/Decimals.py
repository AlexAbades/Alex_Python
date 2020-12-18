# PEP 327

# Other method to represent Real Numbers
# float (0.1) --> Has a Infinite binary expansion but it has a finite decimal expansion

# A Rational number is any number that has a finite number of digits in it. It can be expressed in a fraction way

# We'd like to have an alternative to the (binary) float type to avoid the approximations issues with floats
# But if a number, like 0.1, with an infinite binary expansion is  a rational number, 'cause it has its fraction 1/10
# Why we don't operate with fractions to store all the information?
# If we'd like to sum two fractions 2/10 + 1/15, we'd have to make
# - common denominator: 2/15 + 1/15
# - operation: 3/15
# - reduction: 1/5

# A lot of, complex operations, requires memory

a = float(100.01)
print('Class type')
print(type(a))
print("Memory address")
print(hex(id(a)))

print("precision")
print(format(a, '.25f'))


# Running a billion times. For instance, bank transactions
"""
for a in range(1000000000):
    a += a


print("Once we've done 1 billion operations:")
print(a)

file = open('variable_a.txt', 'w')
file.write(str(format(a, '.25f')))
file.close()
"""


file = open('variable_a.txt')
a = float(file.readline())
print(type(a))
print(format(a, '.25f'))
print(100010000000.00-a)
print("")
# the difference it is significant

# Decimals have a context that controls certain aspects of working with decimals:
# - Precision: Applies to the arithmetic operations
# - Rounding: algorithm

# You can change the precision in a global or in a local context. The first one changes the default context,

import decimal
from decimal import Decimal

g_ctx = decimal.getcontext()  # context object
print(g_ctx)
print(g_ctx.prec)
print(g_ctx.rounding)
# Round Half_even is the float rounding

# Changing global context
print("\nChanging global context")

g_ctx.prec = 6
print(g_ctx)
print(g_ctx.prec)
print("")
g_ctx.rounding = 'ROUND_HALF_UP'
g_ctx.rounding = decimal.ROUND_HALF_UP
# It's the same
print(decimal.ROUND_HALF_UP)
print(type(decimal.ROUND_HALF_UP))
print(g_ctx)
print(g_ctx.rounding)

# Setting to default values
print("\nDefault: ")
g_ctx.prec = 28
g_ctx.rounding = decimal.ROUND_HALF_EVEN
print(g_ctx)

# Changing Local context

l_gtx = decimal.localcontext()
print("")
print("It doesn't return a context, it returns: ")
print(type(l_gtx))
print("")
print("Furthermore, the g_ctx, which was getcontext, returned: ")
print(type(g_ctx))
print("\n\n")
# It returns a context manager with the local method
# we have to work with the WITH statement, it means that once we've done with this with block, that local context that
# we've created it will be dispose of.

x = Decimal('1.25')
y = Decimal('1.35')

print("Local context")
with decimal.localcontext() as ctx:
    print(type(ctx))
    print(ctx)
    ctx.prec = 6
    ctx.rounding = decimal.ROUND_HALF_UP
    print(ctx)
    print("")
    print(decimal.getcontext())
    # It returns the current context that we're working with, in this case, inside the with statement, it's the local
    # context we've created
    print(id(ctx) == id(decimal.getcontext()))
    print("\n\n")
    print("Rounding inside the with statement pre-defined global variables")
    print(round(x, 1))
    print(round(y, 1))
    # It round Up, as we've specified in the local context
    print("\nOutside the with statement, the rounding rule is governed by the HALF_EVEN")
print(round(x, 1))  # Not inside the with statement, round to even
print(round(y, 1))  # Not inside the with statement

print("")
# CONSTRUCTORS
# Decimal(x); where x:

# Integers
x = Decimal(10)
print(x)
print("")

# Other Decimal object
print(y)
print("y type is {0}".format(type(y)))
x1 = Decimal(y)
print(y)

# Strings
print("")
x2 = Decimal('12.054')
print(x2)

# Tuples
print("")
x3 = Decimal((1, (3, 1, 4, 1, 5), -4))
print(x3)

# Floats.
# Kind of useless, those floats that have an infinite binary expression will make that our Decimal instance stores all
# that information, so it won't be an exact Decimal representation of itself
print("")
x3 = Decimal(0.1)
print(x3)
print("\n")
# No use them


# TUPLE CONSTRUCTOR
# +1.23 = + 123*10^-2 --> SIGN, DECIMALS, EXPONENT
# -1.23 = - 123*10^-2 --> SIGN, DECIMALS, EXPONENT
# (S, (d1, d2, d3,...), exp)  sign --> negative(-) = 1. positive(+) = 0
# -3.1415 = (1, (3, 1, 4, 1, 5), -4)


# Context of Precision and the constructor
# Precision affects the arithmetic operations, not the constructor itself
print("Precision")
a = Decimal('0.12345')
b = Decimal('0.12345')
print(a + b)
print("\nChanging precision: ")
with decimal.localcontext() as ctx:
    ctx.prec = 2
    print(a)
    print(b)
    print(a+b)
    c = a + b
    print(c)

print("\nPrinting a variable calculated inside the with statement")
print(c)
# It has a precision of 2, because it was calculated inside the with statement, so it was stored as a decimal with 2
# decimals of precision. Despite of the tha a + b will be the same outside
print(a + b)

import time

a = "3.1415364521"
b = (0, (3 ,1, 4, 1, 5, 3, 6, 4, 5, 2, 1), -10)
n_iter = 10000000


def func(a):
    for i in range(n_iter):
        Decimal(a)
        pass


def cal_time(a):
    start = time.perf_counter()
    func(a)
    end = time.perf_counter()
    lapse = end - start
    return lapse


tple_time = cal_time(b)
string_time = cal_time(a)

print(tple_time)
print(string_time)


