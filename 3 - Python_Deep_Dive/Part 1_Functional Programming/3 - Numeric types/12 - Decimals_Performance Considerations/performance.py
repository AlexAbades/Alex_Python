import sys
from decimal import Decimal

a = 3.1415
print(a)
print(type(a))
print(sys.getsizeof(a))
print("")

b = Decimal('3.1415')
print(b)
print(type(b))
print(sys.getsizeof(b))
# Huge cost in memory

import time


def run_float(n=1):
    for i in range(n):
        a = 3.1415


def run_decimal(n=1):
    for i in range(n):
        a = Decimal('3.1415')


n = 10000000

start = time.perf_counter()
run_float(n)
end = time.perf_counter()
lapse = end-start
print("float: {0}".format(lapse))


start = time.perf_counter()
run_decimal(n)
end = time.perf_counter()
lapse = end-start
print("decimal: {0}".format(lapse))


print("\n\nTime operation")

def run_float(n=1):
    a = 3.1415
    for i in range(n):
        a + a



def run_decimal(n=1):
    a = Decimal('3.1415')
    for i in range(n):
        a + a


n = 10000000

start = time.perf_counter()
run_float(n)
end = time.perf_counter()
lapse = end-start
print("float: {0}".format(lapse))


start = time.perf_counter()
run_decimal(n)
end = time.perf_counter()
lapse = end-start
print("decimal: {0}".format(lapse))


def run_float(n=1):
    a = -3.1415
    for i in range(n):
        a + a



def run_decimal(n=1):
    a = Decimal('-3.1415')
    for i in range(n):
        a + a


n = 10000000

start = time.perf_counter()
run_float(n)
end = time.perf_counter()
lapse = end-start
print("float: {0}".format(lapse))


start = time.perf_counter()
run_decimal(n)
end = time.perf_counter()
lapse = end-start
print("decimal: {0}".format(lapse))

import math


n = 5000000

math.sqrt(a)
def run_float(n=1):
    a = 3.1415
    for i in range(n):
        math.sqrt(a)



def run_decimal(n=1):
    a = Decimal('3.1415')
    for i in range(n):
        a.sqrt()


start = time.perf_counter()
run_float(n)
end = time.perf_counter()
lapse = end-start
print("float: {0}".format(lapse))


start = time.perf_counter()
run_decimal(n)
end = time.perf_counter()
lapse = end-start
print("decimal: {0}".format(lapse))
