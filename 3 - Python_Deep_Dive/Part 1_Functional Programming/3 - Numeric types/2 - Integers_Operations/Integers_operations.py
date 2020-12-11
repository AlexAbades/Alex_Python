# What type of number return the operators

# int + int --> int
# int - int --> int
# int * int --> int
# int ** int --> int
# int / int --> float
# It returns a float even when the division it's exactly

a = 8
print("\n{0} is a {1} type".format(a, type(a)))

b = 4
print("\n{0} is a {1} type".format(b, type(b)))

c = a / b
print("\n{0} is a {1} type".format(c, type(c)))


# To make a division who isn't exactly, we will end with a flot as we've seen above.
# Dividend = 155
# Divisor = 4
# Quotient = 38
# Remainder = 3

# 155/4 = 38 remainder 3
# 155 = 4 * 38 + 3

# If we want to get only the quotient we can use the floor division (div). We can use it if we want the integer or if we
# want after to truncate the number that last one ONLY if we are dealing with positive examples
print("\nThe quotient of 155/4 is: {0}".format(155 // 4))

# If want we want is the remainder we can use the modulo operation (mod), to see if a number is multiple of another,
# or divisor. For example to see if it's odd (3) or even (2)
print("\nThe reminder of 155/4 is: {0}".format(155 % 4))

print(155 == 4 * (155//4) + (155 % 4))
# n = d * (n // d) + (n % d)

# What is the floor division exactly?
# The floor of a real number 'a' is the largest integer LESS than or equal to 'a'.

# floor(3.14) --> 3
# floor(1.99) --> 1

# Look out! If we are dealing with negative numbers.
# floor(-3.14) --> -4  (Is the largest integer lees than or equal! -3 is bigger than -3.1)
print('')
print("Is -3 bigger than -3.1:", 3.1 < -3)
print("Is -4 smaller than -3.1:", -4 < -3.1)
# a // b = floor(a/b)

a = -135
b = 4
print("The division of {0} by {1} is: {2}".format(a, b, a/b))

# If we take a look to the equation, a = b * (a // b) + (a % b)
print("\nThe quotient is the largest int less tan or equal 33.75, which is: {0}".format(-135//4))
print("\nThe reminder is a number which satisfies the above equation, which is: {0}".format(-135 % 4))

# The sign of the mod is the same of the divisor.
import math
from math import floor

print("")
print(floor(4.51654))


def div(a):
    print("The floor number of {0} is: {1}".format(a, floor(a)))


div(3.14)
div(36.99)
div(-3.14)
div(-3.000000000001)

# What happens if we increase the precision of the float number?
# With 13 decimals, 12 of them 0
div(-3.0000000000001)
# If we increase to 16, 15 of them 0?
div(-3.0000000000000001)
# Floats have a limited precision in Python

a = 33
b = 16
print("")
print("Division of {0} by {1}".format(a, b))
print(a/b)
print(a//b)
print(floor(a/b))
# What does the trunc?
print(math.trunc(a/b))

a = -33
b = 16
print("")
print("Division of {0} by {1}".format(a, b))
print(a/b)
print(a//b)
print(floor(a/b))
print(math.trunc(a/b))
# Truncation method drops all the decimal numbers and it only keeps the integer number

print("")
print("{0}/{1} = {2}".format(a, b, a/b))
print("{0}//{1} = {2}".format(a, b, a//b))
print("{0}%{1} = {2}".format(a, b, a % b))
print("{0} = {1} * ({0}//{1}) + ({0} % {1})".format(a, b))


a = 54
b = -5
print("")
print("{0}/{1} = {2}".format(a, b, a/b))
print("{0}//{1} = {2}".format(a, b, a//b))
print("{0}%{1} = {2}".format(a, b, a % b))
print("{0} = {1} * ({0}//{1}) + ({0} % {1})".format(a, b))
