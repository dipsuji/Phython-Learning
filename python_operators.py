# Hello World program in Python

print("Example of Python Operators!\n")
print(" Python Arithmetic Operators\n")
x = 15
y = 3

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)
print(x // y)

print(" Python Assignment Operators\n")
x = 43
x += 3
print(x)
x -= 3
print(x)
x *= 3
print(x)
x /= 3
print(x)
x %= 3
print(x)
x **= 3
print(x)
x //= 3
print(x)

print(" Python Comparison Operators\n")
x = 5
y = 3

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

print(" Python Logical Operators\n")

x = 5
print(x > 3 and x < 10)
print(x > 3 or x < 4)
print(not (x > 3 and x < 10))

print(" Python Identity Operators\n")
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

# is
print(x is z)

# returns True because z is the same object as x

print(x is y)

# returns False because x is not the same object as y, even if they have thew same content

print(x == y)

# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y

# is not
print(x is not z)

# returns False because z is the same object as x

print(x is not y)

# returns True because x is not the same object as y, even if they have the same content

print(x != y)

# to demonstrate the difference betweeen "is not" and "<>": this comparison returns False because x is equal to y

print(x is not z)

# returns False because z is the same object as x

print(x is not y)

# returns True because x is not the same object as y, even if they have the same content
print(x != y)

# to demonstrate the difference betweeen "is not" and "<>": this comparison returns False because x is equal to y


print(" Python Membership Operators\n")
x = ["apple", "banana"]

print("banana" in x)

# returns True because a sequence with the value "banana" is in the list

print("pineapple" not in x)

# returns True because a sequence with the value "pineapple" is not in the list
