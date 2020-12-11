# Theoretically: To minus infinitive to plus infinitive. Without decimals.

# ¿What's the capacity of the computer to store those values? I is no possible to store an infinite value.
# Computer use 0 and 1 to represent integers

# The binary numbers are represented in base 2.
# 2 To the Power:
#   7  6  5  4 3 2 1 0
# 128 64 32 16 8 4 2 1

# _ _ _ _ _ _ _ _  --> 8 Bits
# 0 0 0 1 0 0 1 1 --> (1 * 16) + (0 * 8) + (0 * 4) + (1 * 2) + (1 * 1) = 19
# Representing the decimal value 19 requires 5 bits
# (10011) base 2 = (19) base 10
#
# 8 bits of storage --> 255 only positive [0, (2 to the power of nº bits) - 1]
# With negative, we need 1 bit for the signal. ((two to the 7th power) - 1) --> 127
# [-127, 127]
# what happens with 0? Not considered positive either negative.
# We add that extra number at the bottom --> [-128, 127] by the usual way the numbers are encoded
# [-2 to the 7th power, 2 to the 7th power - 1]

# MEMORY SPACE
# When we create variable in Pythons, it's just a pointer to some address in memory.
# And that pointer it's just an integer number that represents the memory address.
# Those addresses are integers and we need some number of bits to store those numbers.
# In a 32-bit system, it means that it has a 32 architecture and the addresses are limited to a 32 bits integer.
# Every address is a byte, we are looking at the maximum of addresses [0, (2 to the 7th power 32) -1]
# But instead of looking it as integers, we'll look it as byte
# 4294967296 bytes --> 4 Gb

print('Integer type:')
print(type(100))

import sys
import pandas as pd

print("\nsize of the integer 0 in memory: {0} bytes".format(sys.getsizeof(0)))
# It doesn't requires anything to store that number
# Overhead Every time we create a integer, at least we will 24 bytes because the object itself requires some memory
# to get created and stored. And then the number for the memory address.

print("\nSize of the integer number 1: {0} bytes, It uses 4 bytes. We have to take off the "
      "24 bytes of overhead ".format(sys.getsizeof(1)))

print("\nIf we take a look to a large number: ")
print(2 ** 1000)
print("\nThe size of the number in memory  is {0} bytes".format(sys.getsizeof(2 ** 1000)))
print("The number of bits that we had to use to create that number is, 160 - 24 * 8 = {0} bits".format((160 - 24) * 8))

import time
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.style
from random import randint
import math


def calc(a):
    for i in range(10000000):
        a * 2


d = pd.DataFrame(None, range(200), ["number", 'bytes', 'time'])

print(d)
print(len(d.index))
print("\nThe size of the integer 2 is: {0} bytes.".format(sys.getsizeof(2)))


print("\n\nCheck")
a = randint(0, 10)
count = 0


for i in range(100):
    if i == 0:
        start = time.perf_counter()
        calc(0)
        end = time.perf_counter()
        lapse = (end - start) / 10000000
        d['number'][count] = a
        d['bytes'][count] = sys.getsizeof(0)
        d['time'][count] = lapse
        count += 1
    if i != 0 and sys.getsizeof(a) != d['bytes'][count - 1]:
        print(d['bytes'][count - 1])
        start = time.perf_counter()
        calc(a)
        end = time.perf_counter()
        lapse = (end - start) / 10000000
        d['number'][count] = a
        d['bytes'][count] = sys.getsizeof(a)
        d['time'][count] = lapse
        count += 1
    else:
        continue

    max_value = 10 ** (i * 10)
    if max_value > 1000:
        min_value = max_value - 100
    else:
        min_value = max_value * 0.9
    a = randint(min_value, max_value)

print(d)


print(d)
mpl.style.use('seaborn')
plt.plot(d['bytes'], d['time'])
plt.xlabel('Number of Bytes')
plt.ylabel('Number of Seconds: Avg of 10^6 iterations')
plt.show()

# I have to create a code that only evaluates one time a number of x bytes, so then we won't have so much noise in
# the plot

