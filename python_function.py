# Hello World program in Python

print("Python Function\n")


# Creating a Function
# In Python a function is defined using the def keyword:
def my_function():
    print("Hello from a function")


# Calling a Function
# To call a function, use the function name followed by parenthesis:
my_function()

print("Parameters")


# Information can be passed to functions as parameter.
# The following example has a function with one parameter (fname). When the function is called, we pass along a first name,
#  which is used inside the function to print the full name:
def my_function(fname):
    print(fname + " of Employee")


my_function("name")
my_function("Emil")
my_function("salary")


# Default Parameter Value
# The following example shows how to use a default parameter value.
# If we call the function without parameter, it uses the default value:
def my_function(country="India"):
    print("I am from " + country)


my_function("Sweden")
my_function("Japan")
my_function()
my_function("Brazil")


# Return Values
# To let a function return a value, use the return statement:
def my_function(x):
    return 6 * x


print(my_function(4))
print(my_function(5))
print(my_function(10))
