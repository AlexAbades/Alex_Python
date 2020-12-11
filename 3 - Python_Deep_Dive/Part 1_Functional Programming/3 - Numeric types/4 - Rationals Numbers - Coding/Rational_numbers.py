# Rational number are fractions of integer numbers

# 7/2 or -22/7

# Any real number with a finite number of digits after the decimal point is also a rational number.
# 7.5/3 or -54.45/12 a fraction of rational numbers gives a rational number
# 0.45 --> 45/100
# 0.123456789 --> 12345689/100000000
# 8.3/1.4 --> 83/14

# We can represent the rational numbers in Python using the Fractin class in the fractions module
# We can use the constructor tu create an instance of that class
# Numerator --> default value 0
# Denominator --> default value 1

from fractions import Fraction

x = Fraction(3, 4)
print(x)
y = Fraction(22, 7)  # twenty-two over seven
print(y)
z = Fraction(6, 10)
b = Fraction(8, 16)
# Fractions are automatically reduced  by Python, and we can also put the sign either above or below the line.
print(z)
print(b)

a = Fraction(10)
print(a)

z = Fraction(-6, 10)
print(z)
z = Fraction(6, -10)
print(z)
# As it doesn't matter where the sign is, above or below, by convention Python alwways put the sign in the numerator

# we can create fractions of:
# other _fraction
# float
# decimal
# string


# STRINGS
print("\nSome fractions with the string rational number constructor")
x = Fraction('10')  # That will create an integer of value 10, and as the denominator hasn't been specified it will by 1
print(x)
y = Fraction('0.125')  # it will convert the float into a rational number, a fraction.
print(y)
z = Fraction('22/7')
print(z)

# Standard arithmetic operator are supported: +, -, *, / --> and results in Fractions as well
print("\nArithmetic operator +:")
print(z + y)

# Using the denominator and numerator properties of our fraction object.
print("\nWe can get the denominator and numerator: ")
print("The numerator of the fraction {0} is {1}".format(z, z.numerator))
z.numerator
print("The denominator of the fraction {0} is {1}".format(z, z.denominator))
z.denominator

# Float object have a finite precision.
# Any float can be written as a fraction

# Irrational numbers. They are infinite numbers

import math
print("")
print(math.pi)
print(Fraction(math.pi))
print("")
print(math.sqrt(2))
print(Fraction(math.sqrt(2)))
# They both are irrational number, but internally they are represented as floats --> floats are finite numbers, have
# a finite precision.
# The fractions that Python shows us, are going to be an approximation of the irrational number, it will depend on the
# precision of the float number

# CONVERTING FLOAT INTO FRACTION has an important caveat.
# If we are dealing with rational numbers, the fractions will match perfectly with the float representation,
# Bu when er are dealing with irrational numbers, the fraction representation of a specific number won't be the same as
# the irrational number, it would be an approximation of the float number.
# For example:
print('\nFloat number: ')
a = 1/8
print(a)
a = Fraction(a)
print("The fraction is:")
print(a)

print("\nThe irrational fraction 10/3 doesn't have a exact float representation, we can reach:")
a = 10/3
print(a)
print("So when we want to represent that float number, even if we know that the fraction is 10/3, Python will return a "
      "fraction of the float approximiation")
a = Fraction(a)
print(a)


# what happens if we say that the fraction 10/3 is 0.3
a = 0.3
print(format(0.3, '.5f'))
# In reality that's not the number that we are storing
print(format(0.3, '.25f'))

# We can force to get a specific fraction, constraining the denominator.
# using the limit_denominator(max_denominator=1000000) instance method
# It find the closest rational number(which could be precisely equal) with a denominator that doesn't exceed
# max_denominator
print("")
print(math.pi)
x = Fraction(math.pi)
print("Fraction of the number float: {0}, with the denominator constrained to not be greater "
      "than {1}:".format(math.pi, 10))
print(x.limit_denominator(10))
print("Float number is: {0}".format(float(x.limit_denominator(10))))
print("Fraction of the number float: {0}, with the denominator constrained to not be greater "
      "than {1}:".format(math.pi, 100))
print(x.limit_denominator(100))
print("Float number is: {0}".format(float(x.limit_denominator(100))))
print("Fraction of the number float: {0}, with the denominator constrained to not be greater "
      "than {1}:".format(math.pi, 500))
print(x.limit_denominator(500))
print("Float number is: {0}".format(float(x.limit_denominator(500))))

