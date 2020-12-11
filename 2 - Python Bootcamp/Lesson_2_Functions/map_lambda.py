def square(num):
    return num**2

mylist =[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]

print(list(map(square, mylist)))


def splicer(name):
    if len(name)%2==0:
        return 'Even'
    else:
        return name[0]

print(splicer('Hello'))

mynames = 'Jhon Miky Cindy Alexander'.split()

print(list(map(splicer, mynames)))  # The function has to be the first argument, the iterable object, the second.

def even(num):
    return num % 2 == 0

print(list(filter(even, mylist)))


