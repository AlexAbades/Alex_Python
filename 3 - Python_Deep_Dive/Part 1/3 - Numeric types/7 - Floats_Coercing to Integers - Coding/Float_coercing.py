# If we want to take an integer from a float we'll have data loses
# truncation
# floor
# ceiling
# rounding

"""
MAX FLOAT number
import pandas as pd
import sys

x = 250
d = pd.DataFrame(None, range(x), ['BYTES', 'NUMBER'])
a = 24.0

for i in range(x):
    a *= 17.4
    d['BYTES'][i] = sys.getsizeof(a)
    d['NUMBER'][i] = a


print(d)

t = '1' * 10
print(t)
"""

# TRUNCATION
# Simply returns the integer portion of the number, it ignores everything after the decimal point.
import math
a = 10.5
b = 4.257
c = -82.548
d = -0.00000548
print("Truncating numbers with the truncate modulo from math library")
print(math.trunc(a))
print(math.trunc(b))
print(math.trunc(c))
print(math.trunc(d))

# The int constructor, makes exactly the same if we pass a float number.
print("\nTruncating floats with the int contructor")
print(int(a))
print(int(b))
print(int(c))
print(int(d))

# FLOAT
# The floor of a number is the LARGEST integer LESS than (or equal) to the number.
# floor(x) = max{i of Z(integer numbers) | i <= x}
# ---10----(10.4)-------11---
# x = 10.4
# The largest int less than 10.4 is 10

# With negative numbers,
# --(-11)--------(-10.4)----(-10)--
# The largest int less than -10.4 is -11
print("\nFloor numbers")
a = 10.5
b = 4.257
c = -82.548
d = -0.00000548

print(math.floor(a))
print(math.floor(b))
print(math.floor(c))
print(math.floor(d))

# WITH POSITIVE NUMBERS, FLOOR == TRUNCATION
print(math.floor(b)==math.trunc(b))

# NOT FOR NEGATIVE VALUES
print(math.floor(c) == math.trunc(c))

# The floor division
# a // b = floor(a / b)
print("\nIf a and b are floats")
a = 10.5
b = 4.257
print((a // b) == math.floor(a / b))

print("\nIf a and b are int")
a = 10
b = 4
print((a // b) == math.floor(a / b))


# CEILING
# The ceiling of a number is the SMALLER integer GREATER than (or equal) to the number.
# floor(x) = min{i of Z(integer numbers) | i >= x}
# # ---10----(10.4)-------11---
# The smaller integer bigger than 10.4 is 11

# # ---(-11)----(-10.4)-------(-10)---
# The smaller integer bigger than -10.4 is -10
print("\nCeiling numbers")
x = 0.000057
a = 10.5
b = 4.257
c = -82.548
d = -0.00000548

print(math.ceil(x))
print(math.ceil(a))
print(math.ceil(b))
print(math.ceil(c))
print(math.ceil(d))