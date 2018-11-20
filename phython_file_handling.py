print("Python File Open")
# File handling is an important part of any web application.
# Python has several functions for creating, reading, updating, and deleting files.

# File Handling------
# The key function for working with files in Python is the open() function.
# The open() function takes two parameters; filename, and mode.


print("Open a File on the Server")
# To open the file, use the built-in open() function.
# The open() function returns a file object, which has a read() method for reading the content of the file:
f = open("demofile.txt", "r")
print(f.read())

print("Read Only Parts of the File--")
# By default the read() method returns the whole text, but you can also specify how many character you want to return:
# Return the 5 first characters of the file:

f = open("demofile.txt", "r")
print(f.read(5))

print("Read line--")
# You can return one line by using the readline() method:
# Read one line of the file:

f = open("demofile.txt", "r")
print(f.readline())

# By calling readline() two times, you can read the two first lines:
f = open("demofile.txt", "r")
print(f.readline())
print(f.readline())

# By looping through the lines of the file, you can read the whole file, line by line:
# Loop through the file line by line:

f = open("demofile.txt", "r")
for x in f:
    print(x)
