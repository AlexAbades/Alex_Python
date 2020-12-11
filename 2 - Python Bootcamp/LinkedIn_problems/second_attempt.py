fruits = ["apples", "oranges", 'bananas']
quantities = [5, 3, 4]
prices = [1.5, 2.25, 0.89]

groceries = list(zip(fruits, quantities, prices))
print(groceries)

i = 0

output = []

for fruit in fruits:
    temp_qty = quantities[i]
    temp_price = prices[i]
    output.append((fruit, temp_qty, temp_price))
    i += 1
print(output)

i = 0
output = []
for fruit in fruits:
    for qty in quantities:
        for price in prices:
            output.append((fruit, qty, price))
    i += 1

print(output)

# Exercise 2

print('recursive function')
def hi(n=1):
    if n>3:
        return
    print(n)
    hi(n+1)

print(hi())

# Exercise 3 all() function. What does the function do?
# https://beginnersbook.com/2019/03/python-all-function/#:~:text=Python%20all()%20function%20accepts,also%20this%20function%20returns%20true.

# Exercise 4.
# For what we use the self key.
# https://www.google.com/search?q=self+key+python&oq=self+key+p&aqs=chrome.1.69i57j0l7.4899j0j7&sourceid=chrome&ie=UTF-8

# Exercise 5
# Python static method
# https://www.journaldev.com/18722/python-static-method#:~:text=Let's%20get%20started.-,What%20is%20a%20static%20method%3F,an%20object%20for%20that%20class.

# Exercise 6
# zip() function in python

# Exercise 7
# Base case in a recursive function

# Exercise 8:
# PEP 8 coding style
# constant, variables...

# Exercise 9
# Class methods

# Exercise 10
# map() function in python


# Exercise 11
# Stack in python
#https://www.geeksforgeeks.org/stack-in-python/#:~:text=A%20stack%20is%20a%20linear,often%20called%20push%20and%20pop%20.


# Exercise 12
# What is a deque python

# Exercise 13
# Static method

