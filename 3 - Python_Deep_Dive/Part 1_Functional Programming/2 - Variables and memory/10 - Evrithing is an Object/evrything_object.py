# Everything is an Object: True

# Integers(int)
# Booleans(bool)
# Floats(float)
# Strings(str)
# Lists(list)
# Tuples(tuple)
# Sets(set)
# Dictionaries(dict)
# None(Nonetype)

# Operators(+, -, ==, ...)
# Functions
# Classes
# Types


# They are all instances of their own classes.
# A function is an instance of the function class.
# A class defined by the user itself is an instance of the class Class

# All of them have  memory addresses!


# When we create a function, let's say def my_func(): --> my_func is basically our variable name, but is pointing to a
# function object and has the state (the code)

def my_func_1(a):
    return a


def my_func_2(b):
    return b


print("The address of my_func_1 is: ", hex(id(my_func_1)))
print("The address of my_func_2 is: ", hex(id(my_func_2)))

# ANY OBJECT CAN BE ASSIGN TO A VARIABLE (including functions)
# ANY OBJECT CAN BE PASSED TO A FUNCTION AS AN ARGUMENT (functions can be passed in functions)-->Decorators
# ANY OBJECT CAN BE RETURNED FROM A FUNCTION (including functions)

# What does the parentheses in the function?
# my_func --> without parentheses is the name of the function. FUNCTION NAME. (which stores the address)
# my_func() --> with parentheses invokes the function. INVOKES THE FUNCTION

print('\n')
a = 10
print(type(a))  # a is a class of type int instance, 'a' is an int instance
# If 'a' is an int instance, we should be able to create new instances of that class using the standard
# instantiation notation. For create new objects given a class
b = int(10)
print(b)
print(type(b))
# No differences

# classes have documentation
# help(int)

print('\nInstantiate a binary number')
c = int('0101', base=2)  # Base 2: Binary notation 0101--> 0*2^3 + 1*2^2 + 0*2^1 + 1*2^0
print(c)
print('')


def square(a):
    return a ** 2


print('Defining a function')
print(type(square))
print("The memory address of my function square is: ", id(square))

# We can assign the function address to a new variable name

f = square
print("\nThe memory address of my variable name f is: {0}".format(id(f)))

print("f is square?", f is square)

print(square(2))
print(f(2))


def cube(a):
    return a**3


print('\nThe address of my cube function is: {0}'.format(id(cube)))


print("\n\nFUNCTION THAT RETURNS A FUNCTION")


def select_function(fn_id):
    if fn_id == 1:
        return square
    else:
        return cube


f = select_function(1)
print('f is square?', f is square)
print('f is cube?', f is cube)
print('The address of f is: {0}'.format(id(f)))
# Note that we have the same address than the square function. So now f in pointing to the function object
print('\nNow my f function is pointing to the square function object')
print(f(3))
print("\n\n")

f = select_function(0)
print('Setting f to my cube function')
print('f is square?', f is square)
print('f is cube?', f is cube)
print('The address of f is: {0}'.format(id(f)))
print('\nNow my f function is pointing to the square function object')
print(f(3))
print('')

# If we don't want to assign the returned function into a variable we can do the following
print(select_function(2)(4))  # Python first evaluates select_function and it invokes cube with the parameter 3


# FUNCTION PASSED AS A PARAMETER
print("\n\nFUNCTION PASSED AS A PARAMETER")


def exec_function(fn, n):
    return fn(n)

print(exec_function(cube, 4))