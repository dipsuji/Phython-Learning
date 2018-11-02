# Hello World program in Python

print("Introduction\n")

print("Python is a popular programming language. It was created in 1991 by Guido van Rossum.\n")

# python uses indentation to indicate a block of code.                    .
if 5 > 2:
    print("Five is greater than two!")
# Creating Variables.
x = 5
y = "John"
print(x)
print(y)

# Variables do not need to be declared with any particular type and can even change type after they have been set.

xy = 4  # x is of type int
xy = "Sally"  # x is now of type str
print(xy)

# To combine both text and a variable, Python uses the + character:

xx = "awesome"
print("Python is " + xx)

# You can also use the + character to add a variable to another variable:

x1 = "Python is "
y1 = "awesome"
z = x1 + y1
print(z)

# For numbers, the + character works as a mathematical operator:

x2 = 5
y2 = 10
print(x2 + y2)

# But If you try to combine a string and a number, Python will give you an error:

x3 = 5
y3 = "John"
# error line - print(x3 + y3)
