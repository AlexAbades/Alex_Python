def func_one(n):
    return [str(num) for num in range(n)]


print(func_one(10))


def func_two(n):
    return list(map(str, range(n)))

print(func_two(10))


import time

# GRAB CURRENT TIME BEFORE RUNNING THE CODE
start_time = time.time()
# RUN THE CODE
result = func_one(1000000)
# GRAB THE CURRENT TIME AFTER RUNNING THE CODE
end_time = time.time()
# ELAPSED TIME
elapsed_time = end_time - start_time

print('Time 1: ', elapsed_time)
print('')

# GRAB CURRENT TIME BEFORE RUNNING THE CODE
start_time = time.time()
# RUN THE CODE
result = func_two(1000000)
# GRAB THE CURRENT TIME AFTER RUNNING THE CODE
end_time = time.time()
# ELAPSED TIME
elapsed_time = end_time - start_time

print('Time 2: ', elapsed_time)
print('')

# THE PROBLEM WITH THE TIME LIBRARY IS THAT IS THE FUNCTION RUNS TO FAST, IT BECOMES VERY DIFFICULT TO HAVE ACCURACY

# GRAB CURRENT TIME BEFORE RUNNING THE CODE
start_time = time.time()
# RUN THE CODE
result = func_one(10)
# GRAB THE CURRENT TIME AFTER RUNNING THE CODE
end_time = time.time()
# ELAPSED TIME
elapsed_time = end_time - start_time

print('Time 3: ', elapsed_time)
print('')

# GRAB CURRENT TIME BEFORE RUNNING THE CODE
start_time = time.time()
# RUN THE CODE
result = func_two(10)
# GRAB THE CURRENT TIME AFTER RUNNING THE CODE
end_time = time.time()
# ELAPSED TIME
elapsed_time = end_time - start_time

print('Time 4: ', elapsed_time)
print('\n')




# AS WE CAN SEE, IF WE NEED TO COMPARE SIMPLE CODE, WE'LL GET A HUGE ERROR, WE CAN USE INSTEAD
import timeit

# stmt --> what we want to run
# setup --> What code need to be run before we call the statement

# FUNCTION ONE
stmt = """
func_one(100)
"""

setup = """
def func_one(n):
    return [str(num) for num in range(n)]
"""

result_func_one = timeit.timeit(stmt, setup, number=1000000)
print('Time to run function one 1.000.000 times is: ', result_func_one)
print('')


# FUNCTION TWO
stmt2 = """
func_two(100)
"""

setup2 = """
def func_two(n):
    return list(map(str, range(n)))
"""

result_func_one = timeit.timeit(stmt2, setup2, number=1000000)
print('Time to run function two 1.000.000 times is: ', result_func_one)
print('')

