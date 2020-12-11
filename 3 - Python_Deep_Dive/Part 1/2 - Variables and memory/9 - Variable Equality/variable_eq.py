# How we could compare two variables?

# First: We could look at the memory address, are this two variable pointing to the same object?
# identity operator "is" --> compares memory addresses
# negation "is not" or "not(var_1 is var_2)"

# Second: Compare the internal state of the object. They could have different memory addresses but have the same state
# equality operator "==" --> compares the state of the object
# negation "!=" or "not(var_1 == var_2)"


def share_reference(a, b):
    if a is b:
        print("The value 'a' and the value 'b' share the same reference: {0}".format(hex(id(a))))
    else:
        print("The value 'a' and the value 'b' do not share the same reference \n"
              "Reference 'a': {0}\nReference 'b': {1}".format(hex(id(a)), hex(id(b))))


def share_state(a, b):
    if a == b:
        print("The value 'a' and the value 'b' share the same state: {0}".format(a))
    else:
        print("The value a and the value b do not share the same state \n"
              "State 'a': {0}\nState 'b': {1}".format(a, b))


a = 10
b = a

share_reference(a, b)
share_state(a, b)
print('')


print('Mutable objects: lists')
a = [1, 2, 3]
b = [1, 2, 3]
share_reference(a, b)
print('')
share_state(a, b)

print('\n\nFloat vs integer\n')
a = 10
b = 10.0
share_reference(a, b)
share_state(a, b)


# None object: assigned to variables to indicate that they are not set (empty, null pointer). Nonetheless None is a
# real object managed by the python memory manager
# Furthermore, the memory manager will always use a shared reference when assigning a variable to None.
print('\n\n')
a = None
b = None
c = None
print('The type of None is: ',type(None))
share_reference(a, None)
share_state(a, None)

print('\n')
x = 10
share_reference(x, None)
share_state(x, None)


# Integers
print('\n\n')
a = 10000
b = 10000
share_reference(a, b)
share_state(a, b)