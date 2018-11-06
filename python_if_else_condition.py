# Hello World program in Python

print("Python Conditions and If statements----------\n")
# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b

# If statement:
a = 343
b = 505
if b > a:
    print("b is greater than a")

# Elif:
# The elif keyword is pythons way of saying "if the previous conditions were not true, then try this condition".
a = 53
b = 53
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")

# Else
# The else keyword catches anything which isn't caught by the preceding conditions.  
a = 150
b = 73
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")

# You can also have an else without the elif:
a = 150
b = 73
if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

#  Short Hand If
# If you have only one statement to execute, you can put it on the same line as the if statement.
a = 43
b = 50
if b > a: print("b is greater than a")

# And
# The and keyword is a logical operator, and is used to combine conditional statements:
a = 200
b = 33
c = 500
if a > b and c > a:
    print("Both conditions are True")

# Or
# The or keyword is a logical operator, and is used to combine conditional statements:    
a = 100
b = 43
c = 300
if a > b or a > c:
    print("At least one of the conditions are True")
