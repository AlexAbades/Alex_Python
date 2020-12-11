# The memory management, garbage collection and optimizations, are usually specific to the Python implementation.
# In this course we're going to ise CPython, the standard (or referee) Python implementation (written in C)

a = 10
b = 10


def namestr(obj, namespace):
    return [name for name in namespace if namespace[name] is obj]


def reference(s):
    name = namestr(s, globals())
    print('The reference for {0} its: # = {1}, and the value of the object is: {2}'.format(name, id(s), s))


reference(a)

# INTERNING: Reusing objects on demand
# At startup, Python(CPython), pre-loads(caches) a global list of integers in the range [-5, 256] (different in
# this version)
# Anytime we reference or use an integer in that range Python is going to use the cash version of that object.
# Re-use that memory address.
# SINGLETON objects (classes that can only be instantiate once)
# Optimization strategy --> Small integers show often in the code, so it won't have to create the object, only point it.

"""
When it compiles the module it is able to recognize that the two (immutable) objects 500 are the same - and so it 
ends up re-using the same object. 
If you were to set a = 500 in one module, b=500 in another module and import one module into the other you would 
observe that the objects are not the same - but because they are defined in the same module you see that behavior. 
When you run things in interactive Python (and that's essentially what Jupyter is - a front-end to that), 
the same optimizations are not always possible. """

a = 10
b = int(10)
c = int('10')
d = int('1010', 2)

print(a, b, c, d)
print(a is b and b is c and c is d)
print(id(a), id(b), id(c), id(d))