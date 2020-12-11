# To test for "equality" of two different floats, you could do the following methods:

# Use the round method in both sides of the equation
print("Rounding numbers")
a = 0.1 + 0.1 + 0.1
b = 0.3
print("Extended numbers")
print("a is: ",format(a, '.25f'))
print("b is: ", format(b, '.25f'))
# if we round them
print("\nRounded versions")
print(format(round(a, 5), '.10f'))
print(format(round(b, 5), '.10f'))
print("is a == b?")
print(round(a, 5) == round(b, 5))
print("")


# We can use an appropriate range (epsilon) within the two numbers are deemed equal
# ABSOLUTE TOLERANCE
# for some epsilon > 0, a = b if and only if |a-b| < epsilon
import math
print("Other numbers")
a = 0.1 + 0.1 + 0.1
b = 0.3
print("a is: ",format(a, '.25f'))
print("b is: ", format(b, '.25f'))
print("The difference between them is: ")
s_delta = math.fabs(a-b)
print(s_delta)

print("\n\nLarge numbers")
a = 10000.1 + 10000.1 + 10000.1
b = 30000.3
print("a is: ", format(a, '.25f'))
print("b is: ", format(b, '.25f'))
print("The difference between them is: ")
b_delta = math.fabs(a-b)
print(b_delta)

# With absolute tolerance, we can have for some values positive evaluations and for others false
# if epsilon = 1*10^-15
print("\n\n")
abs_tol = 1e-15
print(abs_tol)
print("For small numbers: ")
print(s_delta < abs_tol)
print("For big numbers: ")
print(b_delta < abs_tol)

# We can compare them with a relative tolerances
print("\nRelative tolerance")
rel_tol = 0.001/100
print(rel_tol)
tol = rel_tol * max(abs(a), abs(b))

a = 0.1 + 0.1 + 0.1
b = 0.3
tol = rel_tol * max(abs(a), abs(b))
print("Tolerance for small numbers: ")
print(tol)

print("Tolerance for big numbers: ")
a = 10000.1 + 10000.1 + 10000.1
b = 30000.3
tol = rel_tol * max(abs(a), abs(b))
print(tol)
print("")

# We would say that if the deference between the numbers is less than our threshold they would be equal
# Problems of the relative tolerances
x = 0.0000000001
print("x=",x)
y = 0
print("y =",y)
# If we use relative tolerance:
rel_tol = 0.1/100
tol = rel_tol * max(abs(x), abs(y))
print("The tolerance is: ",tol)
# The numbers will be equal if the difference between them is lower than the tolerance
print("The tolerance is lower than the difference itself, in this case x")

# Combine both methods! Absolute and relative, and use the larger of the two
# FINAL METHOD
tol = max(rel_tol * max(abs(x), abs(y)), abs_tol)
# PEP 485
# https://www.python.org/dev/peps/pep-0485/

math.isclose(a, b)
# Optionally, the default values are:
# rel_tol = 1e-9
# abs_tol = 0.0

# By default, abs_tot = 0.0 we are only using only the relative tolerance. It won't work well with numbers closer to 0
print("\nIsclose method without specifying a absolute tolerance")
print("\tBig numbers")
x = 1000.0000001
print("x = {0}".format(x))
y = 1000.0000002
print("y = {0}".format(y))
print("is x == y?")
print(math.isclose(x, y))
print("\n\tSmall numbers")
x = .0000001
print("x = {0}".format(x))
y = .0000002
print("y = {0}".format(y))
print("is x == y?")
print(math.isclose(x, y))

print("\nIsclose method with specifying a absolute tolerance: 1e-5")
x = 1000.0000001
print("x = {0}".format(x))
y = 1000.0000002
print("y = {0}".format(y))
print("is x == y?")
print(math.isclose(x, y, abs_tol=1e-5))
print("\n\tSmall numbers")
x = .0000001
print("x = {0}".format(x))
y = .0000002
print("y = {0}".format(y))
print("is x == y?")
print(math.isclose(x, y, abs_tol=1e-5))

# Advantages, we don't have to change the relative and absolute tolerance to get good results with different numbers
print("\nIsclose method with specifying a absolute and relative tolerance: 1e-5")
x = 1000.01
print("x = {0}".format(x))
y = 1000.02
print("y = {0}".format(y))
print("is x == y?")
print(math.isclose(x, y, rel_tol=1e-5, abs_tol=1e-5))
print("\n\tSmall numbers")
x = .01
print("x = {0}".format(x))
y = .02
print("y = {0}".format(y))
print("is x == y?")
print(math.isclose(x, y,rel_tol=1e-5, abs_tol=1e-5))

# IF WE WANT TO COMPARE FLOAT NUMBERS, USE ISCLOSE METHOD
print("\nFinite binary approximations")
x = 0.125 + 0.125 + 0.125
y = 0.375
print("x = {0}".format(x))
print("y = {0}".format(y))
print("If we extend the numbers to 25 digits:")
print("x is: ", format(x, '.25f'))
print("y is: ", format(y, '.25f'))
print("is x == y?")
print(x == y)
print("They are equal if they have finite binary representations")

print("\nFinite binary approximations")
x = 0.1 + 0.1 + 0.1
y = 0.3
print("x = {0}".format(x))
print("y = {0}".format(y))
print("If we extend the numbers to 25 digits:")
print("x is: ", format(x, '.25f'))
print("y is: ", format(y, '.25f'))
print("is x == y?")
print(x == y)
print("They aren't equal if they have finite binary representations")

print("\nRound problem, absolute threshhold")
x = .01
print("x = {0}".format(x))
y = .02
print("y = {0}".format(y))
print("x is: ", format(x, '.25f'))
print("y is: ", format(y, '.25f'))
print("If we round them to 1 significant number")
print(format(round(x, 1), '.10f'))
print(format(round(y, 1), '.10f'))
print("Is x == y")
print(round(y, 1) == round(y, 1))

print("\nRelative threshold problems with islose")
x = 0.01
y = 0.02
print("x = {0}".format(x))
print("y = {0}".format(y))
print("If we extend the numbers to 25 digits:")
print("x is: ", format(x, '.25f'))
print("y is: ", format(y, '.25f'))
print("is x == y?")
print(math.isclose(x, y, rel_tol= 0.01))

print("\nRelative threshold problems")
x = 0.000000000000001
y = 0.000000000000002
print("x = {0}".format(x))
print("y = {0}".format(y))
print("If we extend the numbers to 25 digits:")
print("x is: ", format(x, '.25f'))
print("y is: ", format(y, '.25f'))
print("is x == y?")
print(math.isclose(x, y, rel_tol= 0.01))
# Here we would like to get a True, they are both nearest close to 0

print("\nRelative and absolute threshold")
x = 0.01
y = 0.02
print("x = {0}".format(x))
print("y = {0}".format(y))
print("If we extend the numbers to 25 digits:")
print("x is: ", format(x, '.25f'))
print("y is: ", format(y, '.25f'))
print("is x == y?")
print(math.isclose(x, y, rel_tol=0.01, ))

print('')
x = 0.000000000000001
y = 0.000000000000002
print("x = {0}".format(x))
print("y = {0}".format(y))
print("If we extend the numbers to 25 digits:")
print("x is: ", format(x, '.25f'))
print("y is: ", format(y, '.25f'))
print("is x == y?")
print(math.isclose(x, y, rel_tol=0.01, abs_tol=0.01))

