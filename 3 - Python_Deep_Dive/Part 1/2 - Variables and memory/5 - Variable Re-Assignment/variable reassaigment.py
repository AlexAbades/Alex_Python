# A quick review to dynamic vs static type

# Static type-> languages as C++, Java...
# They have to specify the data type, that will be associated with the
# variable name. We've associated the data type with the variable. Then the variable becomes a references to that
# memory address
# String myVar = 'Hello'
# We can't reassign myVar to a integer, because the myVar it's declared as a string


# Dynamic type --> Python
# We don't specify a data type to the variable, the variable it's just a reference pointing to an object
# my_var = 'hello' --> string object, address = 0x1000
# So we can reassign my_var to a different object type.
# And here we have to keep in mind that we are not changing the type of my_var, because it never had a type. It's just
# a references what it has changed it's the type of the object that it's pointing.

# What Python will do it's create a different object with a different address
# my_var = 10 --> integer object, address = 0x1234


a = 'hello'
print("The variable 'a' is: ", a)
print("The memory address is: ", hex(id(a)))
print("The variable a's type is : ", type(a), "\n")

a = 10
print("The variable 'a' is reassigned to: ", a)
print("The memory address is: ", hex(id(a)))
print("The variable a's type is : ", type(a), "\n")
# Different address from the above code

a = a + 5
print("The variable 'a' is reassigned to: ", a)
print("The memory address is: ", hex(id(a)))
print("The variable a's type is : ", type(a), "\n")
# Different address from the above code

a = lambda x: x**2
print("The variable 'a' is reassigned to: ", a)
print("The memory address is: ", hex(id(a)))
print("The variable a's type is : ", type(a), "\n")

# Tricky thing
a = 10
b = 10
print("The variable 'a' is reassigned to: {0}; and the variable 'b' to: {1}".format(a,b))
print("The memory address of a is {0}; and of b is: {1}".format(hex(id(a)), hex(id(b))))
print("The variable a's type is: {0}; and b's type is: {1}".format(type(a), type(b)))
# They share the same memory address, they are both pointing to the same object.  

