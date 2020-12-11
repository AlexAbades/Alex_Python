# If we ant to pass more than X predefined arguments in a function we have to use *args or **kwargs


def suma(a, b):
    return sum((a, b))  # We have to pass it as a tuple to make the sum


print(suma(40, 60))


# a and b are positional arguments, 40 is assigned to a because it's in the first argument and 60 it's in the second
# argument

def myfunc(a, b, c=0, d=0):
    # we pass more than one argument and we set them to 0, but if we have to be sure what
    # it's gping to do the function to not hider or make a wrong operation, in this case if we make a multiplication
    # it will give us a wrong result
    return sum((a, b, c, d))


print(myfunc(10, 10, 56))

# so we can use *args that it returns a tuple of values


def myfunc(*args):  # We can pass whatever name we want, the important it's the asterisk: *
    print(args)
    return sum(args)*0.05


print(myfunc(1,2,3,10))


# Similarly, Python offers a way to handle arbitrary numbers of keyworded arguments. Instead of creating a tuple of
# values,
#
# **kwargs builds a dictionary of key/value pairs. For example:


def myfunc(**kwargs):
    print(kwargs)
    if 'fruit' in kwargs:
        return ' I would like an {}'.format(kwargs['fruit'])


print(myfunc(food='potato', desert='icecream', fruit='orange'))


# we can use the two arguments

def myfunc(*args, **kwargs):
    print(args)
    print(kwargs)
    return 'I would like {} {} please'.format(args[0], kwargs['food'])


print(myfunc(10, 30, 2, 51, fruit='orange', desert='ice cream', food='hamburgers'))


def myfunc(*args, **kwargs):
    if 'fruit' and 'juice' in kwargs:
        print(f"I like {' and '.join(args)} and my favorite fruit is {kwargs['fruit']}")
        print(f"May I have some {kwargs['juice']} juice?")
    else:
        pass


myfunc('eggs', 'spam', fruit='cherries', juice='orange')

print('\n\n')

def myfunc(*args, **kwargs):
    print(args)
    print(kwargs)
    print('\n')
    if 'place' and 'month' in kwargs:
        print(f"I would like to go around {' or '.join(args)} days to {kwargs['place']}")
        print(f"I think that I would like to go in {kwargs['month']}")
    else:
        pass

myfunc('10', '20', place='Punta cana', month='August')