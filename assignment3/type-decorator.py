# -------- Task 2: A Decorator that Takes an Argument --------------------------------------------------------------
'''
1. Within your assignment3 folder, write a script called type-decorator.py.

2. Declare a decorator called type_converter. It has one argument called type_of_output,
which would be a type, like str or int or float.
It should convert the return from func to the corresponding type, viz:

x = func(*args, **kwargs)
return type_of_output(x)
	
3. Write a function return_int() that takes no arguments and returns the integer value 5.
Decorate that function with type-decorator. In the decoration, pass str as the parameter to type_decorator.

4. Write a function return_string() that takes no arguments and returns the string value "not a number".
Decorate that function with type-decorator. In the decoration, pass int as the parameter to type_decorator.
Think: What's going to happen?

5. In the mainline of the program, add the following:

y = return_int()
print(type(y).__name__) # This should print "str"
try:
   y = return_string()
   print("shouldn't get here!")
except ValueError:
   print("can't convert that string to an integer!") # This is what should happen
'''

def type_converter(type_of_output): #decorator factory
    def decorator(func): #The decorator that will take the function
        def wrapper(*args, **kwargs): #The wrapper that will run the function with its parameters
            result = func(*args, *kwargs)
            return type_of_output(result)
        return wrapper
    return decorator

@type_converter(str)
def return_int():
    return int(5)


@type_converter(int)
def return_string():
    return str("not a number")


y = return_int()
print(type(y).__name__) # This should print "str"
try:
   y = return_string()
   print("shouldn't get here!")
except ValueError:
   print("can't convert that string to an integer!") # This is what should happen
