# Python is creating an object of type integer of value 10 in some memory address (1000) and my_var in a pointer to
# that object, a reference, it's the memory address of that object, 1000.
my_var = 10

print(my_var)
print('\nMemory address id: ')
print(id(my_var))

print("\nWe can convert the memory address id into a hexadecimal version: ")
print(hex(id(my_var)))

print('\n2nd example: ')
greeting = 'hello'
print(greeting)
print('\nId address: ')
print(id(greeting))
print('\nHexadecimal version:')
print(hex(id(greeting)))

# Variable are just memory addresses, they are memory references.
