# An object in python is something that has a type, a state (data) and an address
# Changing the data inside the object is called modifying the internal state of the object.

# We say that an object has mutated if the internal state of the object(data) has changed and the memory address no.

# Mutable --> An object whose internal state can be changed.
# Lists --> We can add, remove or replace elements in that container.
# Sets
# Dictionaries
# User-Defined Class

# Immutable --> AN object whose internal state cannot be changed.
# Numbers (int, float, Booleans, etc) --> we can change a number, as we saw in the previous lesson, we can reassign the
#                                         variable to point to another address with a different object of type int.
# String --> we cannot change the internal state of that string
# Tuple --> We cannot add or remove or replace elements in that container.
# Frozen Sets
# User-Defined Classes

t = (1, 2, 3)  # Immutable, completely frozen
print(t)
print(hex(id(t)))
print(type(t))
print('')

a = [1, 2]  # mutable
print(a)
print(hex(id(a)))
print(type(a))
print('')
b = [3, 4]  # mutable
print(b)
print(hex(id(b)))
print(type(b))
print('')
t = (a, b)  # immutable
print(t)
print(hex(id(t)))
print(type(t))
print('')
a.append(3)
b.append(5)
print('')
print(t)
print(hex(id(t)))
print('')
print(a)
print(hex(id(a)))
print('')
print(b)
print(hex(id(b)))
print('')

print('my_list')
my_list = [1, 2, 3]
print(my_list)
print(id(my_list))
my_list.append(4)
print(my_list)
print(id(my_list))

print('my_list_1')
print('')
my_list_1 = [1, 2, 3]
print(id(my_list_1))
# my_list and my_list_1 don't share the same address even if the have the same object, because as they are mutable
# objects, we would like to change the values of one of them but of the other.
my_list_1 = my_list_1 + [4]  # concatenated. Concatenated two list objects, my_list_1 and [4]
print('')
print('my_list_1 concatenated')
print(id(my_list_1))  # It's not the same as it used to be. It's a different object
# Concatenate doesn't modifies the internal state of an object.
# Append method it modifies the internal state of the object.

my_dict = dict(key1=1, key2='a')
print('')
print(my_dict)
print(id(my_dict))
my_dict['key3'] = 10.5
print('')
print(my_dict)
print(id(my_dict))

# Tuple
print('\nTuple')
print(t)
print(id(t))
print('')
print('id address of the integer inside of the tuple')
print(id(t[0]))


