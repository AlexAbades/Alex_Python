# An integer number is an object - an instance of the int class.

# The int class provides multiple constructors (way to instantiate an instance)
a = int(10)
a = int(-10)
a = 10  # Literal way

# We can pass floats but we'll have to deal with data losses
print("")
a = int(10.9)
print(a)

# We can also pass Booleans
print("")
a = int(True)
print(a)

# As well we can pass string
print("")
a = int('10')
print(a)

# FRACTIONS
import fractions

a = fractions.Fraction(22, 7)
print("")
print(a)
print(float(a))
print(int(a))

# And we can actually specify the base the number in my strings
print("")
a = int('123')
# If we don't specify anything, in would show us a base 10 number. The base parameter hjas to be between 2 - 36
# (123) base 10
print(a)
print("")
a = int("1010", 2)
print(a)
# We are changeing the base representation, we are not changing the number
print("")
a = int("100101", base=2)
print(a)

print("\nIntegers with base 16")
a = int("A12F", base=16)
print(a)
# Not key sensitive
a = int("a12f", base=16)
print(a)

# Python is able to recognize letters, which we can use to encode digits in different bases.
# It uses 0 to 9 --> 10 digits.
# And a to z --> 26 letters.
# That's why the base is limited with 36

# REVERSE PROCESS
# Binary or base 2.
print("")
print("Base 2")
print(bin(10))
# Notice that the sting is '0b1010', the first two terms indicate that the number that the string has inside is a
# binary number
print("Base 8:")
print(oct(10))
print("Base 16:")
print(hex(10))

# It doesn't matter if you pass the prefix, the string base identifier, to instantiate an instance of an integer
print("")
a = int('0b1010', base=2)
print(a)

# We can use the prefixes of different bases to create literal integers in different bases without having to use the
# constructor

print('Literal constructor')
a = 0b1010
print(a)

print("")
a = 0o12
print(a)

print("")
a = 0xa
print(a)

# What about other bases that aren't base 2, 8 or 16?
# CUSTOM CODE

# n: number (base 10)
# b: base (target base)

#  n = b (n // b) * + n % b  --> (n // b) * b + n % b

n = 232
b = 5
# The biggest number that we can represent with base 5 is: 4
print("")
print("With 232 as number")
print(232 // 5)
print(232 % 5)
print("")
# we could say, 232 = 46 * 5 + 2
# 232 = 46 * 5^1 + 2 * 5^0  --> 46 too big
# _ _ _ 2

# We repeat the process with the quotient
print("We continue with 46 as number")
print(46 // 5)
print(46 % 5)
print("")
# 46 = 9 * 5 +1

# 232 = [(9 * 5 + 1) *5^1] + [2 * 5^0]
# 232 = [9 * 5^2] + [1 * 5^1] + [2 * 5^0]  --> 9 is too big

print("We continue with 9 as number")
print(9 // 5)
print(9 % 5)
# 9 = 1 * 5 + 4

# 232 = [(1 * 5 + 4) * 5^2 + [1 * 5^1] + [2 * 5^0]
# 232 = [1 * 5^3] + [4 * 5^2] + [1*5^1] + [2 * 5^0]

# 232 is base 5 is: 1 4 1 2

# What happens if we continue?
print("We continue with 1 as number")
print(1 // 5)
print(1 % 5)
# 5 = 0 * 5 + 1

# 232 = [(0 * 5 + 1) + 5^3] + [4 * 5^2] + [1*5^1] + [2 * 5^0]
# 232 = [0*5^4] + [1 * 5^3] + [4 * 5^2] + [1*5^1] + [2 * 5^0]


import string


# Long way 1 function
def rewrite(n, b):
    if b < 2 or n < 0:
        raise ValueError("No valid number")
    else:
        if n == 0:
            return [0]
        digits = []
        while n > 0:
            m = n % b
            n = n // b
            digits.insert(0, m)  # Insert
        # Encoding
        map = '0123456789' + string.ascii_lowercase
        encoding = ''
        for element in digits:
            encoding += map[element]  # not very efficient, we are creating a new string each time, and re-pointing the
            # encoding variable name to it.
        return encoding


print(rewrite(10, 2))


# Short way 1 function
def rewrite(n, b):
    if b < 2 or n < 0:
        raise ValueError("No valid number")
    if b < 2 or b > 36:
        raise ValueError("Invalid base: 2 <= base <= 36")
    else:
        if n == 0:
            return [0]
        digits = []
        while n > 0:
            m = n % b
            n = n // b
            digits.insert(0, m)  # Insert
        # Encoding
        digit_map = '0123456789' + string.ascii_lowercase
        if max(digits) >= len(digit_map):
            raise ValueError('digit_map is not lon enough to encode the digits')
        return ''.join([digit_map[d] for d in digits])


print(rewrite(3451, 16))


# Short way 3 functions
def from_base10(n, b):
    if b < 2 or n < 0:
        raise ValueError("No valid number")
    else:
        if n == 0:
            return [0]
        digits = []
        while n > 0:
            n, m = divmod(n, b)
            digits.insert(0, m)  # Insert
        return digits

def encode(digits, digit_map):
    if max(digits) >= len(digit_map):
        raise ValueError('digit_map is not lon enough to encode the digits')
    return ''.join([digit_map[d] for d in digits])


def rebase_from10(number, base):
    digit_map = '0123456789' + string.ascii_lowercase
    if base < 2 or base > 36:
        raise ValueError("Invalid base: 2 <= base <= 36")
    sign = -1 if number < 0 else 1
    number *= sign

    digits = from_base10(number, base)
    encoding = encode(digits, digit_map)
    if sign == -1:
        encoding = '-' + encoding
    return encoding




import time


def calc(a):
    for i in range(a):
        rebase_from10(15485483,2)
        pass


start = time.perf_counter()
calc(1000000)
end = time.perf_counter()
lapse = end-start
print("For the 3 part function: {0}".format(lapse))


def calc(a):
    for i in range(a):
        rewrite(15485483,2)
        pass


start = time.perf_counter()
calc(1000000)
end = time.perf_counter()
lapse = end-start
print("For the 1 part function: {0}".format(lapse))