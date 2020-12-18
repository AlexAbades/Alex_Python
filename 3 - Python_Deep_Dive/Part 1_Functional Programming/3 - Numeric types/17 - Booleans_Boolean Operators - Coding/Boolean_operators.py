# Boolean operators are defined to operate on and return Boolean values.

# Every object in Python has a truth value (truthiness)

# For any object we can call bool(X) and bool(Y)
# We don't have to use bool() we can write it X and Y
# What is returned when evaluating these expressions?

# OR --> X or Y
# DEFINITIONS


# TRUTH TABLE

#  X--Y  | X OR Y
#  0  0  |   0
#  0  1  |   1
#  1  0  |   1
#  1  1  |   1


# SHORT-CIRCUITING: If X is truthy, returns X, otherwise Y: Return object itself, it can be a boolean

#   X   Y  |           RULE           |     RESULT
#   0   0  | X is False, so return Y  |       0
#   0   1  | X is False, so return Y  |       1
#   1   0  | X is True, so return X   |       1
#   1   1  | X is True, so return X   |       1

# REAL: If X is truthy, returns X, otherwise EVALUATES Y and return it.
# We never look at the value of Y, and the results matches the truth table
# We don't actually evaluate Y until it has to.

# CONSEQUENCES
#    X        Y    |   X OR Y
#   None    'N/A'  |   'N/A'
#   ' '     'N/A'  |   'N/A'
#  'hello'  'N/A'  |  'hello'

# Ex 1
# a = s or 'N/A':
# if s is None: a = 'N/A'
# if s is ' ': a = 'N/A'
# if s is a string with characters: a = s
# a will be s or 'N/A' if s is None or an empty string


# Ex 2
# a = s1 or s2 or s3 or 'N/A'
# In this case, a will be equal to the first truthy value, and is guaranteed to have a value, since 'N/A' is truthy

# Ex 3
# Let's say we have an integer variable that can't be 0, if it's 0 we want to set it to 1
# a = a or 1


# AND --> X and Y
# DEFINITIONS


# TRUTH TABLE

#  X--Y  | X and Y
#  0  0  |   0
#  0  1  |   0
#  1  0  |   0
#  1  1  |   1

# SHORT-CIRCUITING: If X is falsy, returns X, otherwise return Y: Return object itself, it can be a boolean

#   X   Y  |           RULE           |     RESULT
#   0   0  | X is False, so return X  |       0
#   0   1  | X is False, so return X  |       0
#   1   0  | X is True, so return Y   |       0
#   1   1  | X is True, so return Y   |       1

# REAL: If X is falsy, returns X, otherwise EVALUATES Y and return it

# CONSEQUENCES
#    X        Y    |   X and Y
#   10       20/X  |      2
#   0        20/X  |      0

# Seems like we are able to avoid a division by zero error using the and operator
# x = a and total/a  --> if a is gather than 0, it will do the Division, if not it will return a


# sum, n  --> sometimes n is non-zero, sometimes it isn't
# In either case: avg = n and sum/n

#  You want to return the first character of a string s, or an empty sting if the sting is None or Empty
# Option 1
# if s:
#   return s[0]
# else:
#   return ''

# Option 2
# s = s and s[0] --> If s is None, it will return None

# Option 3
# s = (s and s[0]) or ' ' --> If s is None will return X, None. Then it will evaluate with the or operator.
# As X is None, it will return Y, in this example ' '.


# It returns the object based on their True values

# Boolean NOT
# Is a built-in function that returns a Boolean value

# not X --> True if X is falsy
# not X --> False if X truthy

# It can take objects, but it will return the not of the truth value of the object

# [] --> not [] = True
# [1, 2] --> not[1, 2] = False
# None --> not None = Truth

print("OR")
print('a' or [1,2])
print('' or [1,2])

print(1 or 1/0)
# div by 0 won't evaluate 'cause 1 is truth

s1 = None
s2 = ''
s3 = 'abc'

s1 = s1 or 'N/A'
s2 = s2 or 'N/A'
s3 = s3 or 'N/A'
print("")
print(s1, s2, s3)

print("")
print([] or [0])

print("")
print("AND")
print(0 and 100)
print(None and 100)
print([] and [0])


a = 2
b = 4
print(a/b)
# a/b in general, but if b=0, return 0
b=0
print(b and a/b)


s1 = None  # --> not indexable
s2 = ''
s3 = 'abc'

print("And operator")
s1 = s1 and s1[0]
s2 = s2 and s2[0]
s3 = s3 and s3[0]
print(s1)  # --> We don't want to return the empty string
print(s2)
print(s3)

print("And with or operators")
s1 = s1 and s1[0] or ''
s2 = s2 and s2[0] or ''
s3 = s3 and s3[0] or ''
print(s1)  # --> We don't want to return the empty string
print(s2)
print(s3)


print('\nNOT operator')

print(not True)
print(not False)

print("with objects:")
print(bool('abc'))
print(not(bool('abc')))
print(not 'abc')

print("")
print(bool(''))
print(not(bool('')))
print(not '')

print("")
print(bool(None))
print(not(bool(None)))
print(not None)