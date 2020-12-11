# one.py

# when we call this file, a .py, all the code that it's in indentaition level 0, it's going to get run.

# Built in variables are variables that are as __name-of-the-variable__, like:  __name__ and gets assigned a string
# depending on how we are running the file.

# When we run a python file, python assigns implicitly the variable __name__ = '__main__'  (in the background)

# If the python file it's run it directly, then python assigns __name__ = '__main__'


def func():
    print("FUNC() IN ONE.PY")


print("TOP LVL IN ONE.PY")


if __name__ == '__main__':
    print("ONE.PY IS BEING RUN DIRECTLY")
else:
    print("ONE.PY HAS BEEN IMPORTED")