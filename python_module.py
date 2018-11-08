# Hello World program in Python

print("Example of Python Module")
# Consider a module to be the same as a code library.
# A file containing a set of functions you want to include in your application.

# Create a Module---
# To create a module just save the code you want in a file with the file extension .py:
# Save this code in a file named mymodule.py

# (((((->   def greeting(name):
#  print("Hello, " + name)    <-))))))

# Use a Module----
# Now we can use the module we just created, by using the import statement:
import mymodule

mymodule.greeting("Alex")

# Variables in Module----
# The module can contain functions, as already described, but also variables of all types (arrays, dictionaries, objects etc):


# Import the module named mymodule, and access the employee dictionary:
import mymodule

a = mymodule.employee["age"]
print(a)

# You can create an alias when you import a module, by using the as keyword:
import mymodule as mx

a = mx.employee["age"]
print(a)

# Built-in Modules
# There are several built-in modules in Python, which you can import whenever you like.

# Import and use the platform module:
import platform

x = platform.system()
print(x)

print("Using the dir() Function")
# There is a built-in function to list all the function names (or variable names) in a module. The dir() function:
import platform

x = dir(platform)
print(x)

print("Import From Module")
# You can choose to import only parts from a module, by using the from keyword.
# The module named mymodule has one function and one dictionary:
from mymodule import employee

print(employee["age"])
