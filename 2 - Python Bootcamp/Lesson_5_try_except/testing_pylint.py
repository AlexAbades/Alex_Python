"""
A VERY SIMPLE FILE TO EXPLORE PYLINT:
As you begin to expand to larger multi-file projects or you begin to work with a team that's
bigger than just yourself it becomes really important to have tests in place. This way as you
or your teammates make changes or update your code you can run your test files to make sure previous
code still runs as expected. HOW TO CALL THE REPORT:
pylint testing_pylint.py -r y IN THE COMMAND LINE
"""


def my_func():
    """
    Function two print two numbers
    :return: first, second printed
    """
    first = 1
    second = 2
    print(first)
    print(second)


my_func()
