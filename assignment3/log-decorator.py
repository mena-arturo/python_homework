# -------- Task 1: Diary Writing and Testing a Decorator -----------------------------------------------------------
'''
Within the assignment3 folder, create a file called log-decorator.py. It should contain the following.

Declare a decorator called logger_decorator. This should log the name of the called function (func.__name__),
the input parameters of that were passed, and the value the function returns, to a file ./decorator.log.

(Logging was described in lesson 1, so review this if you need to do so.)

Functions may have positional arguments, keyword arguments, both, or neither.
So for each invocation of a decorated function, the log would have:

function: <the function name>
positional parameters: <a list of the positional parameters, or "none" if none are passed>
keyword parameters: <a dict of the keyword parameters, or "none" if none are passed>
return: <the return value>
Here's a cookbook on logging:

# one time setup
import logging
logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log","a"))
...

# To write a log record:
logger.log(logging.INFO, "this string would be logged")

Declare a function that takes no parameters and returns nothing. Maybe it just prints "Hello, World!".
Decorate this function with your decorator.

Declare a function that takes a variable number of positional arguments and returns True.
Decorate this function with your decorator.

Declare a function that takes no positional arguments and a variable number of keyword arguments,
and that returns logger_decorator. Decorate this function with your decorator.

Within the mainline code, call each of these three functions, passing parameters for the functions that take
positional or keyword arguments. Run the program, and verify that the log file contains the information you want.
'''

# Step 1
import logging

# Step 2
logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.DEBUG)

logger.addHandler(logging.FileHandler("./decorator.log","a"))


def logger_decorator(func):

    def wrapper(*args, **kwargs):
        logger.info(f"Function: '{func.__name__}'")
        logger.info(f"Positional parameters: '{args}'")
        logger.info(f"Keyword parameters: '{kwargs}'")
        result = func(*args, **kwargs)
        logger.info(f"Return: '{result}'")
    return wrapper

# Step 3

@logger_decorator
def hello_world():
    print (f"Hello World!")
hello_world()


@logger_decorator
def positional_params(*args):
    return True

positional_params(3, 6, 9)

@logger_decorator
def named_params(**kwargs):
    return logger_decorator
named_params(first='a', second='b', third='c')
