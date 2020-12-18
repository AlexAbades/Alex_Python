# floor and mod --> // and %

# n = d * (n // d) + (n % d)

# For integers the // operator performs a floor division:  a // b = floor(a/b)

# For Decimals the // operator performs a truncated division: a//b = trunc(a/b)
# It really changes for negative numbers
print("Integer floor division:\n")
print("\tPositive values")
a = 10
print(a)
print(type(a))
b = 3
print(b)
print(type(b))
print(" 10 // 3 = {0}".format(a // b))
print("")
print("\tNegative values")
a = -10
print(a)
print(type(a))
b = 3
print(b)
print(type(b))
print(" -10 // 3 = {0}".format(a // b))

import decimal
from decimal import Decimal

# FLOOR

print("\n\nDecimal floor division:\n")
print("\tPositive values")
a = Decimal(10)
print(a)
print(type(a))
b = Decimal(3)
print(b)
print(type(b))
print(" 10 // 3 = {0}".format(a // b))
print("")
print("\tNegative values")
a = Decimal(-10)
print(a)
print(type(a))
b = Decimal(3)
print(b)
print(type(b))
print(" -10 // 3 = {0}".format(a // b))
# Note the difference in the negative values
# a/b --> a = dividend; b= divisor

# How it works the divisions for decimals ?
# 1st - figures out the sign of the result
# 2nd - Use absolute values for division and dividend
# 3th - Keep subtracting b from a as long a >= b
# 4th - Returns the number of times this was performed

# 10/3 --> result is going to be (+)
# 10 - 3 = 7 (7>=3) --> 7 - 3 = 4 (4 >= 3) --> 4-3 = 1 (1 >= 3) NO, stops!
# Returns 3

# -10/3 --> result is going to be (-)
# # 10 - 3 = 7 (7>=3) --> 7 - 3 = 4 (4 >= 3) --> 4-3 = 1 (1 >= 3) NO, stops!
# # Returns -3

# MOD
print("\nIntegers")
n = -135
print(n)
print(type(n))
d = 4
print(d)
print(type(d))
print("\nInteger MOD:")
print(n%d)

print("\nDecimals")
n = Decimal(-135)
print(n)
print(type(n))
d = Decimal(4)
print(d)
print(type(d))
print("\nDecimal MOD")
print(n%d)


# DIV MOD
print("\nIntegers")
n = -135
print(n)
print(type(n))
d = 4
print(d)
print(type(d))
print("Floor and MOD:")
print(divmod(n, d))

print("\nDecimals")
n = Decimal(-135)
print(n)
print(type(n))
d = Decimal(4)
print(d)
print(type(d))
print("Floor and MOD:")
print(divmod(n, d))


# That's because the equation:n = d * (n // d) + (n % d).  Always remains True

# Not all functions in the math module are defined in Decimal class.
# If we use functions of the math module and we apply them in the Decimal class, we'll end with the same problems as
# floats, the decimals numbers will store all float information
import math
print("\n\n")
print("\nmath module operations")
x = 2
print(x)
print(type(x))
print(format(x, '.27f'))

x_dec = Decimal('2')
print(x_dec)
print(type(x_dec))
print(format(x_dec, '.27f'))

root = math.sqrt(x)
print("\nmath module float number")
print(format(root, '.27f'))
print("math module decimal number")
root_mixed = math.sqrt(x_dec)
print(format(root_mixed, '.27f'))
print("decimal module, decimal number")
root_dec = x_dec.sqrt()
print(format(root_dec, '.27f'))

print("if we make the square of the root, we should expect to get the same number")
print("square of of the math module root with float number")
print(format((root*root), '.25f'))
print("square of the math module root with decimal number")
print(format((root_mixed*root_mixed), '.25f'))
print("square of the decimal module root with decimal number")
print(format((root_dec*root_dec), '.25f'))

# Precise
print("\n")
x = 0.01
print(x)
print(type(x))
print(format(x, '.25f'))

x_dec = Decimal('0.01')
print(x_dec)
print(type(x_dec))
print(format(x_dec, '.25f'))

root = math.sqrt(x)
print("\nmath module float number")
print(format(root, '.25f'))
print("math module decimal number")
root_mixed = math.sqrt(x_dec)
print(format(root_mixed, '.25f'))
print("decimal module, decimal number")
root_dec = x_dec.sqrt()
print(format(root_dec, '.25f'))

print("if we make the square of the root, we should expect to get the same number")
print("square of of the math module root with float number")
print(format((root*root), '.25f'))
print("square of the math module root with decimal number")
print(format((root_mixed*root_mixed), '.25f'))
print("square of the decimal module root with decimal number")
print(format((root_dec*root_dec), '.25f'))
# We see that the numbers coming from the math module, those with binary bases, are not the same! Very close, but not
# exactly

print("\nDECIMAL")
a = Decimal('1.5')
print(a.ln())
print(a.exp())
print(a.sqrt())

print("\nFLOAT")
b = 1.5
print(math.log(b))
print(math.exp(b))
print(math.sqrt(b))