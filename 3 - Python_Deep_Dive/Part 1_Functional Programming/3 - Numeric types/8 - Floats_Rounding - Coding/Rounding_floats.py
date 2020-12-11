# ROUND
# two parameters:
# round(x, n=0)
# It will round the number x to the closest multiple of 10^-n

# If n is not specified, then it defaults to 0, and round(x) will return always an int
# 10^0 = 1 --> it will return a multiple of one

# But if n is specified, in won't return always an int, it will return a number of the same type as x
import math

# DEFAULT --> int
a = 1.23
b = round(1.23)
print(a)
print("a rounded by default is:", b, ", an integer")
print("")

# n = 0
# Round to the closest multiple of 10^0 = 0
a = 1.23
b = round(1.23, 0)
print(a)
print("10^0 = {0}".format(10**0))
print("'a' rounded with n=0 is:", b, ", a float")
print("")

# n > 0
a = 1.23
b = round(1.23, 1)
print(a)
print("10^-1 = {0}".format(10**-1))
print("'a' rounded with n=1 is:", b, ", a float")
print("")

# n < 0
# E.G. n = -1
a = 18.2
b = round(a, -1)
print(a)
print("10^1 = {0}".format(10**1))
print("'a' rounded with n=-1 is:", b, ", a float")
print("")

# TIES
# What happens if the number that we want to round it falls just in the middle (0.5 of the decimal we're rounding)
# No closest value. We have to choose, away from zero.
# 1.25 --> 1.3
# -1.25 --> -1.3
# ROUNDING TO NEAREST, WITH TIES AWAY FROM 0


# IN PYTHON IT DOESN'T WORK LIKE THAT, it does:

# BANKER'S ROUNDING IEEE 754 standard:
# Round to the nearest value, with ties rounded to the nearest value with an even least significant digit
a = 1.25
b = round(a, 1)
print(a)
print("10^-1 = {0}".format(10**-1))
print("'a' rounded with n=1 is:", b, ", a float")
print("")

a = 1.35
b = round(a, 1)
print(a)
print("10^-1 = {0}".format(10**-1))
print("'a' rounded with n=1 is:", b, ", a float")
print("")

a = -1.25
b = round(a, 1)
print(a)
print("10^-1 = {0}".format(10**-1))
print("'a' rounded with n=1 is:", b, ", a float")
print("")

a = -1.35
b = round(a, 1)
print(a)
print("10^-1 = {0}".format(10**-1))
print("'a' rounded with n=1 is:", b, ", a float")
print("")

a = 15
b = round(a, -1)
print(a)
print("10^1 = {0}".format(10**-1))
print("'a' rounded with n=1 is:", b, ", a float")
print("")

a = 25
b = round(a, -1)
print(a)
print("10^1 = {0}".format(10**-1))
print("'a' rounded with n=1 is:", b, ", a float")
print("")

# Why Bankers's Rounding?
# Less biased than ties away from zero. In a hypothetical situation, where we have billions of values being rounded,
# if we always round away from 0, will get a higher bias than round on the even
a = 0.5
b = 1.5
c = 2.5
print(a)
print(b)
print(c)
print("\nIf we calculate the average of the above 3 numbers, will get:")
print((a + b + c) / 3)
print("If we would like to round them first, will get")
print("Normal round, 0.5 --> 1, 1.5 --> 2; 2.5-->3")
print("The average is: ", (1+2+3)/3)
print("Banker's round, 0.5-->0; 1.5-->2; 2.5-->2")
print("The average is: ",(0+2+2)/3)

# WHAT IF WE'D LIKE TO ROUND AWAY FROM 0

# VERSION 1.0


def away_from(a):
    if a >= 0:
        sign = 1
    else:
        sign = -1
    return math.trunc(sign * (abs(a) + 0.5))


print("\nRounding away from 0 with positive values:")
print(away_from(10.4))
print(away_from(10.5))
print(away_from(10.6))

print("\nRounding away from 0 with negative values:")
print(away_from(-10.4))
print(away_from(-10.5))
print(away_from(-10.6))


# VERSION 2.0


def away_from(a):
    if a >= 0:
        sign = 1
    else:
        sign = -1
    return int(a + 0.5 *sign)


print("\nRounding away from 0 with positive values:")
print(away_from(10.4))
print(away_from(10.5))
print(away_from(10.6))

print("\nRounding away from 0 with negative values:")
print(away_from(-10.4))
print(away_from(-10.5))
print(away_from(-10.6))


# we can storage a sign with the math.copysign(x, y) function
# It returns the magnitude (absolute value) of x but with the sign of y


# VERSION 3.0


def away_from(a):
    if a >= 0:
        sign = 1
    else:
        sign = -1
    return int(a + math.copysign(0.5, a))


print("\nRounding away from 0 with positive values:")
print(away_from(10.4))
print(away_from(10.5))
print(away_from(10.6))

print("\nRounding away from 0 with negative values:")
print(away_from(-10.4))
print(away_from(-10.5))
print(away_from(-10.6))

print("\nRounding 888.88 to the closest of 10.000 multiple")
print(round(888.88, -4))
print("As 888.88 is less than 5.000 it will be round it to 0")