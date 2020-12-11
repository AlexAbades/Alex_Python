# Float class is Python default implementation for representing real number

# Float uses a fix number of bytes that can be use to store and represent floating point numbers.
# Uses 8 bytes  --> 64 bits
# It also have some overhead like the integer number at the time that the object is created.
# And it's also 24 bytes, no matter how big the number is while it fits on the float description.
# CPython in 3.6v 64 bits


# How are this 64 bits used in the float storage?
# sign   --> 1 bit  0/1
# exponent --> 11 bits  can be in the range [-1022, 1023]
# significant digits --> 52 bits which means 15-17 significant digits (base 10) digits (0-9)

# What are significant digits?
# All digits except leading or trailing zeros


# Numbers of 5 significant digits
a = 1.2345
b = 1234.5
c = 12345000000  # The trailing zeros are stored in the exponent space
d = 0.00012345  # The leading zeros are stored in the exponent space
d = 12345e-50
e = 12345e10

print(d)

# We can represent numbers as a base-10 integers and fractions
# 0.75 --> 7/10 + 5/100 --> Two fractions with non zero numerators. 2 significant digits.
# We can represent it --> 7*10^-1 + 5*10^-2

# 3 significant numbers
# 0.256 = 2/10 + 5/100 + 6/1000
# 0.256 = 2 * 10^-1 +5*10^-2 + 6*10^-3

# significant digits
f = 123.456
# 123.456 = 1*100 + 2*10 + 3*1 + 4/10 + 5/100 + 6/1000
# 123.456 = 1*10^2 + 2*10^1 + 3*10^0 + 4*10^-1 + 5*10^-2 + 6*10^-3

# number = (-1)^sign * sum (di*10^i) -- > i = -m to n
# sign = 0 for positive

import matplotlib.pyplot as plt
import matplotlib.image as mping

img = mping.imread("general_equation.JPG")
imgplot = plt.imshow(img)
plt.show()

# some images cannot be represented using a finite number of terms
# Irrational numbers --> pi, sqrt(2)...
# Rational numbers --> 10/3

# How can we represent those numbers instead of base 10, in base two --> Binary
# (0.11) base 2 -->base 10: (1/2 + 1/4) = 1*2^-1 + 1*2^-2 = (0.50 + 0.25) = 0.75
# (0.1101) base 2 --> base 10: (1/2 + 1/4 + 0/8 + 1/16) = 1*2^-1 + 1*2^-2 + 0*2^-3 + 1*2^-4 = 0.8125
plt.imshow(mping.imread("binary_representation.JPG"))
plt.show()
# we also have certain numbers which we cannot representable with the binary base
# (0.1) in base 10 --> (0.0 0011 0011 0011 0011 0011...) base 2


print(float(10))
print(float('12.5'))

from fractions import Fraction

a = Fraction('22/7')
print(float(a)) # we have to create the fraction first

x = 0.1
print(x)
# If we want to be sure
print(format(x, '.25f'))  # It's an approximation, it coul de higer or lower

y = 1/8
print(format(y, '.25f'))  # Exact representation


# We have to be careful with that
print("\n")
a = 0.1 + 0.1 + 0.1
b = 0.3
print("a is: ", a)
print("b is: ", b)
print("Is a == b: ", a == b)
print("a is really equal to: ",format(a, '.25f'))
print("b is really equal to: ",format(b, '.25f'))