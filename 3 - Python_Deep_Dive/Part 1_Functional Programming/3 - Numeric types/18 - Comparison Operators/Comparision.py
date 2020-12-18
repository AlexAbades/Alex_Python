# Categories of Comparision Operators

# Binary operators
# evaluate to a bool value

# Identity operators: is / is not  --> compares memory address - any type


# Value comparision: == / != --> Compares values, different types OK, but must be compatible.
# Will work with all numeric types.
# Mixed types (except complex) supported
# 10.0 == Decimal('10.0') --> True
# 0.1 == Decimal('0.10') --> False. In binary we son't have an exact representation of 0.2
# Decimal('0.125') == Fraction(1,8) --> True
# True == 1  --> True
# True == Fraction(3 ,3)  --> True

# a == b == c --> a == b and b == c


# Ordering comparision: < / <= / > / >= --> Doesn't work for all types.
# Mixed types (except complex) supported
# 1<3.14
# Fraction(22, 7) > math.pi
# Decimal('0.5') <= Fraction(2, 3)

# a < b < c --> a < b and b < c


# Membership Operations: in / not in --> used for iterable types


print(0.1 is (3 + 4j))
print(3 is 3)
print([1, 2] is [1, 2])
print('a' in 'this is a text')
print(3 not in [1, 2, 3])

print('key1' in {'key1': 1})
print(1 in {'key1': 1})

print(4 == 4 + 0j)
print(4.3 == 4.3 + 0j) # Remember complex are floats we'll have the same problem

3 < 2 < 2/0

import string
print('A'<'a'<'z'>'Z')

print('A'<'a'<'z'>'Z' in string.ascii_letters)



