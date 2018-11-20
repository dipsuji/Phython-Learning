print("Delete a File")
# To delete a file, you must import the OS module, and run its os.remove() function:
# Remove the file "demofile.txt":

import os

os.remove("myfile.txt")

# Check if file exist, then delete it:

import os

if os.path.exists("demofile.txt"):
    os.remove("demofile.txt")
else:
    print("The file does not exist")
