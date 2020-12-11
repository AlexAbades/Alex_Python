f = open('practice.txt', 'w+')
f.write('This is a string test')
f.close()

######################################
# OS
######################################
import os
# Get the current working directory
print('Current directory: ')
print(os.getcwd())
print('')

print('Get a list of all the files in this directory: ')
print(os.listdir())
print('')

print('Get all the files in another directory, C:\\Users')
print(os.listdir('C:\\Users'))
print('')

# HOW WE CAN MOVE FILES INSIDE DIRECTORIES

######################################
# SHUTIL
######################################

import shutil

# shutil.move('practice.txt', 'C:\\Users\\Alex Abades')

print('List of files in current directory: ')
print(os.listdir())
print('')

print('List of files on C:\\User\\Alex Abades')
print(os.listdir('C:\\Users\\Alex Abades'))

# DELETING FILES
# os.unlink(path) which deletes a file at the path your provide

# os.rmdir(path) which deletes a folder (folder must be empty) at the path your provide

# shutil.rmtree(path) this is the most dangerous, as it will remove all files and folders contained in the path.
# All of these methods can not be reversed! Which means if you make a mistake you won't be able to recover the file.
# Instead we will use the send2trash module. A safer alternative that sends deleted files to the trash bin instead of
# permanent removal.


# Instead of deleting permanently the file, we can use the below module, which sends to the trash or bin,
# so we can after recuperate the file

import send2trash

# shutil.move("C:\\Users\\Alex Abades\\PycharmProjects\\untitled\\Exercises\\Udemy\\Python "
#            "bases\\Lesson_7_ExtraModules\\Guess_game.py",
#            "C:\\Users\\Alex Abades\\PycharmProjects\\untitled\\Exercises\\Udemy\\Python bases\\Project_1")


send2trash.send2trash('C:\\Users\\Alex Abades\\practice.txt')

# We can go through all the sub directories and files in a directoryos with os.walk
path = 'C:\\Users\\Alex Abades\\Documents\\Python\\Udemy\\Python\\Complete-Python-3-Bootcamp-master\\12-Advanced Python Modules\\Example_Top_Level'

for folder, sub_folders, files in os.walk(path):

    print(f'Currently looking at {folder}')
    print('\n')
    print('The sub folders are: ')
    for sub_fold in sub_folders:
        print(f'\tsubfolder: {sub_fold}')

    print('\n')
    print('The files are: ')
    for f in files:
        print(f'\tFile: {f}')
    print('\n')


#################################
# DATETIME
#################################
import datetime

mytime = datetime.time(2, 20)

print('My time is: ', mytime)
# As we created an datetime object, we can call some of it's attributes
print('My time minute is: ', mytime.minute)
print('My time hour is :', mytime.hour)
print('My time seconds is: ', mytime.second)
# If we don't provide some information, it will fill it, in the above case above it fill automatically the seconds

print('')
mytime2 = datetime.time(5)

print('My time is: ', mytime2)
print('My time minute is: ', mytime2.minute)
print('My time hour is :', mytime2.hour)
print('My time seconds is: ', mytime2.second)

print('')
mytime3 = datetime.time(14, 45, 34, 899)
print('My time is: ', mytime3)
print('My time minute is: ', mytime3.minute)
print('My time hour is :', mytime3.hour)
print('My time seconds is: ', mytime3.second)

print('')
print('The type of my object date time is: ', type(mytime3))
# It's a time datetime.time object, it only has vales of time information, if we want date information we can
# add some information using a date object or combine it date-time object

print('')
today = datetime.date.today()
print('Today is: ', today)
# We can create our own datetime.date object specifying the date
yesterday = datetime.date(2020, 7, 13)
print('')
print('Yesterday was: ', yesterday)

print('')
print("Today's year is: ", today.year)
print("Today's month is: ", today.month)
print("Today's day is: ", today.day)

print('Another way to print the time is: ')
print(today.ctime())

from datetime import datetime
print('')
mydate = datetime(2020, 4, 12, 23, 34, 54, 23)
print('My date is: ', mydate)

mydate = mydate.replace(month=10, year=2019)
print('\nMy correct date is: ', mydate)
print('\n')

##### How to see for example how much time a person has spent in our web site:
# DATE

from datetime import date

date1 = date(2021, 10, 31)
date2= date(2020, 10, 31)


result = date1 - date2

print(result)
print('my result type is: ', type(result))
# It's a delta object, it has special properties
print('The number of days are: ', result.days)

# DATETIME

datetime1 = datetime(2021, 10, 31, 14, 35, 35)
datetime2 = datetime(2020, 10, 31, 5, 27, 48)
result1 = datetime1-datetime2
print('My result is: ', result1)
print('My total seconds are between hours are: ', result1.seconds)


##############################
# MATH MODULE
##############################
print('\n\n\n')
print('Math Methods')

import math

print(math.floor(4.7))
print(math.ceil(4.2))
print(round(4.3))
print(round(4.5))

# The round function, works depending if it's even or odds

print(round(5.5))  # Odd number
print(round(7.5))  # Odd number
print(round(8.5))  # Even number

# We can find a lot of the mathematical content in Numpy

from math import pi, e, inf, nan

print(pi,'\n', e,'\n', inf,'\n', nan)

print(math.log(e))
print('')
print(math.log(100, 10))
# what it's doing the log it's
print('To what number i have to made the power of 10 to get 100\n10 to the power of 2 it is: ', 10**2)
print(math.log(100, 3))
print(3**4.19180654857877)

print(math.sin(10))
print(math.degrees(pi/2))
print(math.radians(180))

##########################
# RANDOM
##########################

import random

print(random.randint(0, 100))
print('\n')
# We can specify  seed to get always the same number in the randint method

random.seed(101)
print('My number is: ', random.randint(0, 100))
print('My number is: ', random.randint(0, 100))
print('My number is: ', random.randint(0, 100))


# Grab a random item from  list
print('')
mylist= list(range(0,20))
print(mylist)
print(random.choice(mylist))
print(mylist)
print('')

# SAMPLE WITH REPLACEMENT

print('With replacement', random.choices(population=mylist, k=10))
# WE CAN SEE MORE THAN ONCE A NUMBER


# SAMPLE WITHOUT REPLACEMENT
# WE CAN'T SEE MORE THAN ONCE A NUMBER

print('without replacement', random.sample(population=mylist, k=10))

random.shuffle(mylist)
print('My list shuffled ', mylist)

print(random.uniform(a=0, b=100))  # continuous distribution, floating numbers are allowed
# Every number between a and b, have the same likelihood

print(random.gauss(mu=0, sigma=1))


#######################
# PYTHON DEBUGER
#######################

import pdb

# We have to specify it before the error

x = [1,2,3]
y = 2
z = 7

y+z
pdb.set_trace()
# type q to quit

x+z






