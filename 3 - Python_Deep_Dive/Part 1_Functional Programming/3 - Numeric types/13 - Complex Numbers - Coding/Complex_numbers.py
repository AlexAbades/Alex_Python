# complex Class

# Constructor
# complex(x, y)
# x --> Real part
# y --> Imaginary part

# Literal
# x + yj/J

# Both of them are floats, same issues as floats

import sys

a = complex(10, 5)
print(a)
print(type(a))
print(sys.getsizeof(a))

print("")
b = 5 + 7j
print(b)
print(type(b))
print(sys.getsizeof(b))

print("")
print(b.real)
print(type(b.real))
print(b.imag)
print(type(b.imag))

print("")
print(b.conjugate())

# Standard arithmetic works well with complex numbers, they are polymorphic
# Div and mod operator (//) and (%)

print("")
print(a)
print(a + 5)
print(a + 5j)
print(a * 5)

# Comparision operators: == and != work fine, but they have the same problem as floats
# Comparision operators: <, >, <=, >= are not supported
print("\nComparision")
a = complex(1, 2)
print(a)
print(hex(id(a)))
b = 1 + 2j
print(b)
print(hex(id(b)))
print(a == b)
print(a is b)

# math module nos works
# cmath module is the equivalence

import cmath
import math
# RECTANGULAR TO POLAR

# The angle is given in terms of Pi, (radial) Pi = 180º; -Pi = -180º
# measured clockwise

# to get the phase (angle in radials)
a = -1 + 0j
print("\nPhase of {}:".format(a))
print(cmath.phase(a))
print("Magnitude of {}".format(a))
print(abs(a))

a = -1j
print("\nPhase of {}:".format(a))
print(cmath.phase(a))
print("Magnitude of {}".format(a))
print(abs(a))

a = 1
print("\nPhase of {}:".format(a))
print(cmath.phase(a))
print("Magnitude of {}".format(a))
print(abs(a))

a = 1j
print("\nPhase of {}:".format(a))
print(cmath.phase(a))
print("Magnitude of {}".format(a))
print(abs(a))

a = 1 + 1j
print("\nPhase of {}:".format(a))
print(cmath.phase(a))
print("Magnitude of {}".format(a))
print(abs(a))


# POLAR TO RECTANGULAR
print("\nA polar coordinates where Phi: {0}, and absolute: {1}".format(math.sqrt(2), math.pi/4))
print(cmath.rect(math.sqrt(2), math.pi/4))


# Euler's Identity
eu_id = cmath.exp(cmath.pi * 1j) + 1
print("\nEuler's identity:")
print(eu_id)

print("As the result is close to 0 but not exactly, because of the floats problems\n"
      "we should use the isclose method from cmath")

print(cmath.isclose(eu_id, 0, abs_tol=0.0001))


a = 0.1j
print(format(a.imag, '.25f'))
print(a + a +a == 0.3)
print(format((a + a + a, '.25f')))
print(format(0.3, '.25f'))
