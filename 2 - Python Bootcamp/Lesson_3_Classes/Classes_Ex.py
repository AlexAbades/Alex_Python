# PROBLEM 1
# Fill in the Line class methods to accept coordinates as a pair of tuples and return the slope and
# distance of the line.
import numpy as np


class Line:

    def __init__(self, coor1, coor2):

        self.coor1 = coor1
        self.coor2 = coor2

    def __str__(self):
        return "I'm a 2D Euclidean space class"

    def di(self):
        """
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        x = x2 - x1
        y = y2 - y1
        """
        x = self.coor2[0]-self.coor1[0]
        y = self.coor2[1]-self.coor1[1]
        return x,y

    def distance(self):
        x,y = self.di()
        return np.sqrt(x**2 + y**2)

    def slope(self):
        x,y = self.di()
        return y/x



coordinate1 = (3, 2)
coordinate2 = (8, 10)

li = Line(coordinate1, coordinate2)

print('Problem 1')
print('The distance between the two coordinates is, ', li.distance())
print('The slope between the two coordinates is, ', li.slope())
print(li)
print('\n')



# PROBLEM 2
# Calculate the area and the surface area from a cylinder

class Cylinder:

    #Class Attribute
    pi = np.pi

    def __init__(self, height=1, radius=1):

        self.height = height
        self.radius = radius

    def area(self):
        return Cylinder.pi * self.radius * self.radius * self.height


    def surface(self):
        ci_area = self.area()/self.height
        return 2 * Cylinder.pi * self.radius * self.height + ci_area*2
c = Cylinder(2, 3)


print('Problem 2')
print('The cylinder area is, ', c.area())
print('The cylinder surface is, ', c.surface())
print('\n\n')

# PROBLEM 3
# Create a bank account class that has two attributes: Owner, Balance
# Two methods: Deposit, Withdraw
# As an added requirement, withdrawals may not exceed the available balance

class Account:

    def __init__(self, owner, balance):

        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f"This is {self.owner}'s account, your currently balance is {self.balance}"

    def deposit(self, amount):

        if type(amount) is int:
            self.balance += amount
            return f'Your currently balance is {self.balance}'
        else:
            return "Please select a valid amount"


    def withdraw(self, amount):
        if type(amount) is int:
            if amount > self.balance:
                return 'You have exceed your currently account balance, please seect another amount'
            else:
                self.balance -= - amount
                return f"Your currently balance is {self.balance}"
        else:
            return "Please select a valid amount"


acco1 = Account('Jose', 1200)
print(acco1)
print(acco1.deposit(65))
print(acco1.withdraw(14))


