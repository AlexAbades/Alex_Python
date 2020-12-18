# PEP 285

# Python has a specific bool Class that is used to represent boolean values
# However, the bool Class ia a subClass of the int Class
# The bool Class inherits from integers, so ir posses all the properties and methods of integers ans add some
# specialized

print("Is bool subclass of int Class")
print(issubclass(bool, int))

# Two constants are defined: True and False
print("\nAre True and False instances from bool Class")
print(isinstance(True, bool))
print(isinstance(False, bool))

# As it is  a subclass of int,
print("\nAre True and False instances of int Class")
print(isinstance(True, int))
print(isinstance(False, int))

# Both constants are singleton objects of type bool
# They store a a memory address which points to an object in memory of bool type, and that object has some internal
# value: a int of value 1. False is the same thing, but value 0. Both they have more functionality
print("")
print(hex(id(True)))
print(hex(id(False)))
# Because they are singleton objects, they will always retain the same memory address throughout the life time of our
# application
# You can use the identity (is) or equality (==)

# Since bool are also int they can also be interpreted as the integers 1 and 0.
print("")
print(int(True))
print(int(False))

# IMPORTANT: True and 1, or False and 0 are not the same objects, not the same types, different memory addresses
print("\nTrue is 1?")
print(hex(id(True)))
print(hex(id(int(True))))
print(True is 1)
print("\nFalse is 0?")
print(hex(id(False)))
print(hex(id(int(False))))
print(False is 0)

# The internal value are the same even if they aren't the same object, the state is the same!
print("\nIs True == 1")
print(True == 1)
print("Is False == 0")
print(False == 0)

print("\nTypes")
print(hex(id(3<4)))
print(type(3 < 4))
print(hex(id(3<4)))

# That's because the polymorphism
print("\nPolymorphism and strange code:")
print(True > False)
print((1 == 2) == False)
print(((1 == 2) == 0))
print(True + True + True)
print((True + True + True) % 2)
print(-True)

# Bool constructor
# bool(x)
# Returns True when x is True
# Returns False when x is False

# Seems something stupid, but is not.
# Every Class in Python implements something called "Truth value" or "truthyness"
# What is basically saying and asking a class:
# If I were to ask you how you would describe yourself as a boolean what would you say?


# Integers have a truth value defined according to this rule:
# If the integer is 0, the truth value is False, otherwise Truth
# bool(0) --> False (0 is falsy)
# bool(x) --> True for any int x != 0 ( x is truthy)
print("")
print(bool(5))
print(bool(452))
print(bool(-57))
print(bool(0))
