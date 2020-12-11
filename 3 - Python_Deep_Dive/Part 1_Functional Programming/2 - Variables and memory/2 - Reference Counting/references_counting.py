import sys
import ctypes

# We can keep track of these objects that are created on memory, and how many variables are pointing to that same object

my_var = 10
print("\nId reference of my_var: ", id(my_var))
print("Hexadecimal interpretation of my_var's id: ", hex(id(my_var)))

other_var = my_var
# It doesn't take the value "10" and assigning it to other_var
# What it's really doing the code in the above line is, taking the reference of my_var and assigning that reference
# to the new variable other_var. So we are not creating a new object, both variables names are sharing the same refrence
print("\nId reference of other_var: ", id(other_var))
print("Hexadecimal interpretation of other_var's id: ", hex(id(other_var)))
# We don't have wo different objects with value ten.
# The counter of references pointing to the same object will increase to two in this case

#     Reference   |    Count
# ---------------------------
# 0x7ffaba9ca2b0  |      2


# If for some reason the my_var goes away, even if it's because we've assigned to None, or because the python system
# management itself has remove it, the counter will drop to 1, because we still have other_var with that reference
# If other_var disappears, Python realizes that there's no address pointing to that object in memory and erases the
# object


# How to get the reference count.
# sys.getrefcount(my_var)
# That function increases the counter of the variable by 1, because the simple fact of passing my_var trough the
# function creates another references to the variable
print("\nThe count of the reference 0x7ffaba9ca2b0 is: ")
print(sys.getrefcount(my_var))

# Another method that we can use to get the count of that address, is the following method
print("\nThe count of the reference 0x7ffaba9ca2b0 is: ")

print("\n\nList variable id is: ")
a = [1, 2, 3]
print(id(a))
print('\nHexadecimal id: ')
print(hex(id(a)))
print("\nThe count of the variables pinting to that object is: ")
print(sys.getrefcount(a))


# Keep in mind that as we are passing the variable name and not the address, we are going to have one more instance
# pointing to that object


def ref_count(address: int):
    return ctypes.c_long.from_address(address).value


print("\nThe count of the reference ", id(a), " is: ")
print(ref_count(id(a)))
# Keep in mind that first we run the "id" function, but we don't have a count of 2 even if we passed the variable name
# into the id function (remember that each time that we pass the reference to another function we should have two names
# sharing the same reference. In this case the "id" function runs first but once it finished it release its pointer to
# that memory address. The pointer has gone.

b = a
print("\nThe variable id of b is: ")
print(id(b))
print("\nThe count of the reference ", id(a), " is: ")
print(ref_count(id(b)))
c = b
print("\nThe count of the reference ", id(a), " is: ")
print(ref_count(id(c)))
# If we rewrite a variable name like the code below, we are rewriting the address that that name is storing
c = 10
print("\nThe count of the reference ", id(a), " is: ")
print(ref_count(id(a)), "We have a, and b pointing to that object")
# None is an object stored in memory
b = None
print("\nThe new address of b pointing to that None object is: ")
print(id(b))

a_id = id(a)
a = None  # The memory manager frees up that memory address, so we don't know what a_id is storing.
print("\nThe count of that memory address, once we dropped the value of a, is: ")
print(ref_count(a_id))
print("\nIf we run it again...")
print(ref_count(id(a)))
print("\nAnd again...")
print(ref_count(id(a)))

# No matter what, once that counter of memory address reaches 0, Python destroys the object stored in memory
