# Hello World program in Python

print("Example of Python Strings\n")
# Get the character at position 1 (remember that the first character has the position 0):

a = "Hello, World!"
print(a)
print(a[0])
print(a[1])
print(a[2])
print(a[3])

# Substring. Get the characters from position 2 to position 5 (not included):

b = "Hello, World!"
print(b[2:5])

# The strip() method removes any whitespace from the beginning or the end:
a = "    Hello, World!    "
print(a.strip())  # returns "Hello, World!"

# The len() method returns the length of a string:

a = "Hello, World!"
print(len(a))

# The lower() method returns the string in lower case:

a = "HelLo, WoRld!"
print(a.lower())

# The upper() method returns the string in upper case:

a = "Hello, World!"
print(a.upper())

# The replace() method replaces a string with another string:

a = "Hello, World!"
print(a.replace("H", "J"))
