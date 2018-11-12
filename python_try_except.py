# Hello World program in Python

print("Python Try Except")
# The try block lets you test a block of code for errors.
# The except block lets you handle the error.
# The finally block lets you execute code, regardless of the result of the try- and except blocks.

# The try block will generate an exception, because x is not defined:
# Without the try block, the program will crash and raise an error:
try:
    print(x)
except:
    print("An exception occurred")

print("Handling Many Exceptions------")
# Print one message if the try block raises a NameError and another for other errors:

try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")

print("use of else----")
# You can use the else keyword to define a block of code to be executed if no errors were raised:
# In this example, the try block does not generate any error:

try:
    print("Hello")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")

print("use of Final block----")
# The finally block, if specified, will be executed regardless if the try block raises an error or not.
try:
    print(x)
except:
    print("Something went wrong")
finally:
    print("The 'try except' is finished")

# The try block will raise an error when trying to write to a read-only file:

try:
    f = open("demofile.txt")
    f.write("Lorum Ipsum")
except:
    print("Something went wrong when writing to the file")
finally:
    f.close()

# The program can continue, without leaving the file object open
