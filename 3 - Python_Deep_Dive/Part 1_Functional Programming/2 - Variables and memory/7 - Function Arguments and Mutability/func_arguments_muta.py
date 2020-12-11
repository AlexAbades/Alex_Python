# Immutable objects are safe from unintended side effects.
# Strings are immutable
my_var = 'hello'
# We have my var pointing to a specific address
print('The address of my_var is: ')
print(hex(id(my_var)))
print('')


def process(s):
    s = s + ' world'
    return s


print(process(my_var))
print('')


# Module scope
# my_var --> 'hello' string object that we have in memory 0x1000

# process() cope, the parameter 's' it's initially pointing to my_var, because it's 'hello'
# s --> my_var pointing at 0x1000
# But at the moment tht the function does its function, concatenate strings, as the string is immutable it can't
# change, so the 's' parameter must point to a new object.

# process () scope
# s  --> 'hello world' object that we've created in memory 0x1234
# We have safety in this process because string is a immutable object.


# Mutable objects are NOT safe from unintended side-effects


def process(lst):
    lst.append(100)


my_list = [1, 2, 3]
process(my_list)

# Module scope
# my_list --> '[1, 2, 3]' list object that we have in memory 0x1000

# process() scope
# lst --> '[1, 2, 3]' list object that we have in memory 0x1000

# Once the function has done its function
# process() scope
# lst --> '[1, 2, 3, 100]' list object that we have in memory 0x1000
# The object has mutated


# We have changed the state of my_list
print(my_list)


# Immutable object
def process(s):
    print('Initial s # = {0}'.format(id(s)))
    s = s + ' world'
    print('Final s # = {0}'.format(id(s)))
    print(s)


print('\n')
my_var = 'hello'
print('my_var # = {0}'.format(id(my_var)))
print('')
process(my_var)
print('\nmy_var # = {0}'.format(id(my_var)))
# It has not changed
print(my_var)
print('')


# Mutable object
def modify_list(lst):
    print('Initial lst # = {0}'.format(id(lst)))
    lst.append(100)
    print('Final lst # = {0}'.format(id(lst)))
    print(lst)


my_list = [1, 2, 3]
print(my_list)
print('my_list # = {0}'.format(id(my_list)))
print('')
modify_list(my_list)
print('my_list # = {0}'.format(id(my_list)))
# As we modified the state the memory address is the same.


# Modify tuple
def modify_tuple(t):
    print('Initial t # = {0}'.format(id(t)))
    t[0].append(100)
    print('Final t # = {0}'.format(id(t)))
    print(t)


my_tuple = ([1, 2], 'a')

print('\nTuple')
print(my_tuple)
print('my_tuple # = {0}'.format(id(my_tuple)))
print('')
modify_tuple(my_tuple)
# The memory address is remains the same 
