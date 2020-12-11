# Sometimes the Python memory manager system doesn't work well.

# Circular References

# my_var (points to) --> Object A (var_1) point to --> Object B
# If we set my_var to 0, the count of object A goes down to 0 and it gets destroyed, and so object B, there's nothing
# pointing to it

# But what happens if the Object B is pointing to Object A (Circular reference)?
# If we destroy, set to None my_var, the counter of Object A will drop to 1, because now Object B it's also pointing
# to it, so it won't get destroyed by reference counting, as it, Object B will still have the counter on 1, 'cause
# Object A is pointing to him. Reference counting won't be able to destroy that circular reference and we'll have a
# memory leak.

# Here gets in the GARBAGE COLLECTOR
# You can interact the garbage collector using the "gc". By default it's tuned ON, but you can turn it OFF
# (not recommendable), you'll turn it off for performing reasons, by default it runs periodically once every minute
# or so.
# You can call it manually and do your own clean up

# Versions below 3.4 have __del__ problem collectible

import ctypes
import gc


def ref_count(address):
    return ctypes.c_long.from_address(address).value


def object_by_id(object_id):
    for obj in gc.get_objects():  # This basically will look at all the object in the garbage collection
        if id(obj) == object_id:
            return "Object exists"
    return "Not Found"


class A:
    def __init__(self):
        self.b = B(self)  # The "b" variable it's going to be equal to an instance of the class B, passing self to that
        # instance (self in this context means A, an instance of A).
        # We'll pass an instance of A to B, and in B's constructor we'll store this reference.
        # self.b it's going to be an instance of the future class B passing the instance of A.
        print("A: self: {0}, b: {1}".format(hex(id(self)),hex(id(self.b)))) # We are going to print out the memory
        # address of the instance of A (ourselves) and the memory address of the B instance
#############
# self refers to the instance of each class
#############


class B:
    def __init__(self, a):  # Takes in an extra parameter (let's call it a), it's what it's passed when B gets
        # constructed, line 39 B(self)
        self.a = a
        print("B: self: {0}, a: {1}".format(hex(id(self)), hex(id(self.a))))


gc.disable()

print("\nThe references of the classes are: ")
my_var = A()

print("\nWe can print the reference of my A instance, my_var, is: ")
print(hex(id(my_var)))

print("\nWe can print the reference of the B instance, which is initialized inside of my A instance (my_var) \nand is "
      "stored in the 'b' variable: my_var.b. The B class instance is stored in the b variable.")

print("\nThe reference of my B instance which is initialized in my A instance is:", hex(id(my_var.b)))

print("\nWe can also get the reference of the A instance, from the instance of the class B.")
print("It's stored in the 'a' variable of the B instance (my_var.b), so to reach the reference of my_var we should\n"
      "get the a variable form the class B instance (which is my_var.b")

print("\nThe reference of my A instance (my_var) is:", hex(id(my_var.b.a)))

# I need to hold references of a and B
a_id = id(my_var)
b_id = id(my_var.b)

print("\n\na_id:",hex(a_id))
print("b_id:", hex(b_id))

# We need to store them because if we get rid of my_var, we won't be able to reach them.

print("\nCount of a_id is:", ref_count(a_id))  # We have to variables pointing to A, my_var and the instance of B
print("Count of b_id is:", ref_count(b_id))


print("\nDoes the object 'a_id' exists in the garbage collection?", object_by_id(a_id))
print("Does the object 'b_id' exists in the garbage collection?", object_by_id(b_id))

my_var = None
print("\nWe set to None my_var")
print("\nCount of a_id is:", ref_count(a_id))
print("Count of b_id is:", ref_count(b_id))

print("\nDoes the object 'a_id' exists in the garbage collection?", object_by_id(a_id))
print("Does the object 'b_id' exists in the garbage collection?", object_by_id(b_id))

gc.collect()
print("\nWe enable the garbage collect")
print("\nDoes the object 'a_id' exists in the garbage collection?", object_by_id(a_id))
print("Does the object 'b_id' exists in the garbage collection?", object_by_id(b_id))

print("\nCount of a_id is:", ref_count(a_id))
print("Count of b_id is:", ref_count(b_id))

print("\nIf we try it again...")
print("\nCount of a_id is:", ref_count(a_id))
print("Count of b_id is:", ref_count(b_id))
print("We no longer know what are storing both variables; a_id, b_id ")
