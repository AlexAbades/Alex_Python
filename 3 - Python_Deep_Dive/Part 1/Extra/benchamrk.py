"""
Benchmark of operators
"""

import pandas as pd
import time
from random import randint
import sys
import numpy as np
n_iter = 10000000


def calc_prod(a):
    for i in range(n_iter):
        a * 2
        pass


def calc_sum(a):
    for i in range(n_iter):
        a + a
        pass


def calc_rest(a):
    for i in range(n_iter):
        a - a
        pass


def calc_power(a):
    for i in range(n_iter):
        a ** 2
        pass


def calc_division(a):
    for i in range(n_iter):
        a / 2
        pass


index_length = range(30)
matrix_columns = ['Bytes', 'Prod Time', 'Sum Time', 'Rest Time', 'Power Time', 'Div Time']
index_counter = 0
numbers = pd.DataFrame(None, index_length, ['Numbers'])
data = pd.DataFrame(0.0, index=index_length, columns=matrix_columns)
# Take care, if we create a matrix with NaN values, when we want to restore them it will give the SettingWithCopyWarning
print("the len of the matrix is")
print(len(data))
print("The length of numbers is:")
print(len(numbers))
# Quick check to the matrices
print(data[:5])
print("\ndata size is: {0}".format(data.shape))
print(numbers[:5])
print("\nnumbers size is: {0}".format(numbers.shape))

dic = {
    calc_prod: 'Prod Time',
    calc_sum: 'Sum Time',
    calc_rest: 'Rest Time',
    calc_power: 'Power Time',
    calc_division: 'Div Time'
}

# Create random numbers with different weights
# 2 to the power of nº of bits
# Pc operates with packages of 4 bytes, so the multiplying factor should be 16, 4*4
i = 0
while index_counter != numbers.shape[0]:
    if index_counter == 0:
        numbers['Numbers'][i] = 0
        index_counter += 1
    else:
        min_value = 2 ** (15*i+2)
        max_value = 2 ** (15*(i+1)) - 1
        n = randint(min_value, max_value)
        if sys.getsizeof(n) > sys.getsizeof(numbers['Numbers'][index_counter-1]):
            numbers['Numbers'][index_counter] = n
            index_counter += 1
    i += 1

# Quick check to the numbers and store their weight in the data list
data['Bytes'] = list(map(lambda x: sys.getsizeof(x), numbers['Numbers']))
print(numbers)
print("\nBytes of data column")
print(data['Bytes'])

# pass the function without parentheses

def time_calc(calc_func):
    for element in range(len(numbers)):
        start = time.perf_counter()
        calc_func(numbers['Numbers'][element])
        end = time.perf_counter()
        lapse = (end-start)/n_iter
        print(lapse)
        data[dic[calc_func]][element] = lapse  # No esta asignando valor pq es float
        print(data[dic[calc_func]][element])



time_calc(calc_prod)
print(data)
print(data['Prod Time'])
print(format(data['Prod Time'][4],'.25f'))


"""

for i in index_length:
    if i == 0:
        start = time.perf_counter()
        calc_prod(0)
        end = time.perf_counter()
        lapse = (end - start) / 10000000
        data['Number'][index_counter] = a
        data['Bytes'][index_counter] = sys.getsizeof(0)
        data['Prod Time'][index_counter] = lapse
        index_counter += 1
    if i != 0 and sys.getsizeof(a) != data['Bytes'][index_counter - 1]:
        start = time.perf_counter()
        calc_prod(a)
        end = time.perf_counter()
        lapse = (end - start) / 10000000
        data['Number'][index_counter] = a
        data['Bytes'][index_counter] = sys.getsizeof(a)
        data['Prod Time'][index_counter] = lapse
        index_counter += 1
    else:
        continue
    max_value = 10 ** (i * 10)
    if max_value > 1000:
        min_value = max_value - 100
    else:
        min_value = max_value * 0.9
    a = randint(min_value, max_value)

# If I check the bytes that a number uses, we can make bigger the range of the randi
# Also I can make a function that storages the time calculation

print(data[:][:10])
"""