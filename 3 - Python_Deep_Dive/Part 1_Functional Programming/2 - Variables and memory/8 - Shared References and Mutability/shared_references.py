# Shared references
# Sharing references it's safe whenever the object is completely immutable.

a = 10
b = a
# we are setting the "b" reference to the memory address of "a"


def namestr(obj, namespace):
    return [name for name in namespace if namespace[name] is obj]


def reference(s):
    name = namestr(s, globals())
    print('The reference for {0} its: # = {1}, and the value of the object is: {2}'.format(name, id(s), s))


reference(a)
# We can see that they are sharing the same reference and the same space in memory

# If I modify b or a, the only way of doing it is creating a new object on that variable name

b = 20
print('')
print('The memory address of b is now: # {0}'.format(id(b)))
print('While the memory address of a remains: # {0}'.format(id(a)))
print('')
reference(a)
reference(b)
print("\n\n")

# They no longer share references


# What happens when we use a motable object?

a = [1, 2, 3]
b = a
reference(a)
# But what happens when we append something, or we modify one of the values.
b.append(100)
print('\nThe value of b it is now {0}'.format(b))
print('')
reference(b)
# The reference remains the same, they are both pointing to the some object mutated, 'casue the state of that object
# has now changed. The value of "a" is the same of b
print("\nThe value of 'a' has changed because we've modified 'b', the value of 'a' is: {0}\n\n".format(a))

# What happens if instead of append we concatenate?
b = b + [4]
print("The value of 'b' now is: {0}".format(b))
reference(b)
# It has a different reference than a because we have created another object, we have not mutated the object
reference(a)
print('\n')

# What if we set the same values to different names
a = 10
b = 10
reference(a)
# They point to the same object because they are immutable, and if we would like to change one of both, we must have
# to create a new object.
print('\n')
a = [1, 2, 3]
b = [1, 2, 3]
reference(a)
reference(b)
# They don't share references, because if we'd like to change the value of one of them, as they are mutable objects we
# wouldn't have to create a new object, we could change the state of that object.
# They have different references or addresses




