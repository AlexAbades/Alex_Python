# It's used to allow the program to continue with the code indifferently that there's an error or not.

print("Attempt one:")
try:
    # Want to attempt this code
    # May have an error
    result = 10 + '10'
except:
    print("Hey, it seems you aren't adding correctly")
else:
    print('Add went well')
    print(result)
print('\n')


print("Attempt two")
try:
    result = 10 + 10
except:
    print("Hey, it seems you aren't adding correctly")
else:
    print('Add went well')
    print(result)
print('\n')


print('finally word')
try:
    f = open('testfile', 'w')  # It allows to write in that file, and if it's not created, it creates it.
    f.write('Hey I am writing in this file')
except TypeError:
    print('There was a type error!')
except OSError:
    print('Hey you have an OS error!')
finally:
    # Allways it's going to execute, no matter what!
    print('I always run')
print('\n')

print('Finally second attempt, showig an OS error: ')
try:
    f = open('testfile', 'r')  # It allows to write in that file, and if it's not created, it creates it.
    f.write('Hey I am writing in this file')
except TypeError:
    print('There was a type error!')
except OSError:
    print('Hey you have an OS error!')
except:
    # If we don't specify the error type, it's going to be all other exceptions
    print("All other exceptions")
finally:
    # Allways it's going to execute, no matter what!
    print('I always run')
print('\n')


# VALIDATING USER INPUT WITH TRY/EXCEPT AND WHILE LOOP

def ask_for_int():
    try:
        result = int(input('Please provide a number: '))
    except:
        print('Whoops, that is not a number')
    finally:
        print('End of try/except/finally')


def ask_for_int():
    while True: # when we use this syntaxis we always need a break point!!

        try:
            result = int(input('Please provide a number: '))
        except:
            print('Whoops, that is not a number')
            continue
        else:
            print('Valid number')
            break  # It breaks into the loop
        finally:
            print('End of try/except/finally')
            print('I always run at the end!')

# We can mix finally and else statements

ask_for_int()

print('\n\n')
try:
    for i in ['a', 'b', 'c']:
        print(i**2)
except TypeError:
    print("It seems that it's not a number")
print('\n\n')




def division():
    while True:
        try:
            x = int(input('Select a number: '))
            y = int(input('Select another number: '))
            z = x/y
        except ValueError:
            print('Whoops that is not a number')
            continue
        except ZeroDivisionError:
            print("Hey!, You can't divide by 0")
            continue
        else:
            print(z)
            break
division()
print('\n\n')


def power():
    while True:
        try:
            x = int(input("Please eneter a number: "))
            x **= 2
        except ValueError:
            print("An error occurred! You didn't enetered a number, Please try again!")
        else:
            print(f'Thank you, your number squared is {x}')
            break

power()