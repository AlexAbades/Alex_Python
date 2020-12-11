"""
Functions & Decorators
"""


def func():
    return 1


print(func())


def hello():
    return 'Hello'


print(hello())

# Functions are objects that can be passed to other objects

greed = hello

print('\nTesting the hello function: ')
print(hello)
print(hello())

print('\nTesting the greed object: ')
print(greed)
print(greed())
print('\n')
# We can see that the two objects, hello and greed have the same storage in the memory
# <function hello at 0x0000027AE8920F78>


# We delete the name hello
del hello
try:
    print(hello())
except NameError:
    print('NameError: Name hello is not defined')

print('\n')
print('Attempt to call the greed object with the hello object deleted')
print(greed())
print('\n')


# I think that we can call it because we haven't deleted the function, only the name that calls the function


def hello(name='Alex'):
    print('The hello() function has been executed')

    def meliod():
        return '\t The grredo() function has been executed'

    def welcome():
        return '\t\t The welcome() function has been executed'

    print(meliod())
    print(welcome())

    print('This is the end of the hello function')


hello()
print('\n')


# THE COOL THING IS THAT WE CAN RETURN FUNCTIONS, SO WE CAN ASSIGN NEW OBJECTS TO THE FUNCTIONS THAT A FUNCTION RETURN

def hello(name='Alex'):
    print('The hello() function has been executed')

    def greet():
        return '\tThe greet() funtion has been executed'

    def welcome():
        return '\t\tThe welcome function has been executed'

    print('I am going to return a function')
    if name == 'Alex':
        return greet  # Look out! because adding the parentheses, we actually return the function but already executed
    else:
        return welcome


print('Proving the functions return:\n')
my_new_func = hello('Alex')
print('\n')

print(my_new_func)
print(my_new_func())


# Other examples

def meliodas():
    def demon():
        return '\t Meliodas is a demon '

    return demon


new_func = meliodas()
print('\n')
print(new_func)
print(new_func())

# PASSING FUNCTIONS AS ARGUMENTS
print('\n\nTrying a simple function:')


def annex():
    return 'Hello i am Alex'


print(annex)
print(annex())


def house(some_def_func):
    print('I am running another code!')
    print(some_def_func())  # Note here that we are executing now, in this line, the function!


print('\n\nTrying functions as arguments to other functions:')

house(annex)  # Note here that we are not passing the annex function executed! (It hasn't the parentheses)


# DECORATORS
print('\n')


def funcs_need_decorator():
    print('I want to be decorated!!')


def new_decorator(original_func):
    def wrap_func():
        print('Some extra code before the original function')

        original_func()

        print('Some extra code after my original function')

    return wrap_func


print('Probe simple func:')
print(funcs_need_decorator)
funcs_need_decorator()

print('\n')
decorated_func = new_decorator(funcs_need_decorator)  # Note, again, that we don't execute the function

print(decorated_func)
decorated_func()

# Instead of having to define a new object that it's going to be a function's return,
# with another function as an argument, we can call the @ decorator
# Instead of:  decorated_func = new_decorator(funcs_need_decorator)
print('\n\nDecorator example:\n')


@new_decorator
def example_to_be_decorated():
    print('Hello i am an example of a function that needs to be decorated')


example_to_be_decorated()
