print("Write to an Existing File")
# To write to an existing file, you must add a parameter to the open() function:
# "a" - Append - will append to the end of the file
# "w" - Write - will overwrite any existing content

# Open the file "demofile.txt" and append content to the file:
f = open("demofile.txt", "a")
f.write("Now the file has one more line!")

# Open the file "demofile.txt" and overwrite the content:
f = open("demofile.txt", "w")
f.write("Woops! I have deleted the content!")

print("Create a New File")
# To create a new file in Python, use the open() method, with one of the following parameters:
# "x" - Create - will create a file, returns an error if the file exist
# "a" - Append - will create a file if the specified file does not exist
# "w" - Write - will create a file if the specified file does not exist

# Create a file called "myfile.txt":
f = open("myfile.txt", "x")
