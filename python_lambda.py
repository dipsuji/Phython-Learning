# Hello World program in Python

print("Python lambda\n")
# A lambda function that adds 10 to the number passed in as an argument, and print the result:

x = lambda a: a + 10
print(x(5))

# A lambda function that multiplies argument a with argument b and print the result:

x = lambda a, b: a * b
print(x(5, 6))

# A lambda function that sums argument a, b, and c and print the result:

x = lambda a, b, c: a + b + c
print(x(5, 6, 2))


# Use that function definition to make a function that always doubles the number you send in:

def myfunc(n):
    return lambda a: a * n


mydoubler = myfunc(2)

print(mydoubler(11))


# use the same function definition to make both functions, in the same program:

def myfunc(n):
    return lambda a: a * n


mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))

