# Hello World program in Python

print("Python Dictionaries\n")
print("In Python dictionaries are written with curly brackets, and they have keys and values.\n")

# Create and print a dictionary:
thisdict = {
    "name": "Alex",
    "roll_number": "234566",
    "passing_year": 1964
}
print(thisdict)

# You can access the items of a dictionary by referring to its key name:
x = thisdict["roll_number"]
print(x)

# There is also a method called get() that will give you the same result:
x = thisdict.get("roll_number")
print(x)

# You can change the value of a specific item by referring to its key name:
thisdict["passing_year"] = 2018
print(thisdict)

# You can loop through a dictionary by using a for loop.
# Print all key names in the dictionary, one by one:
for x in thisdict:
    print(x)

# Print all values  in the dictionary, one by one:
for x in thisdict:
    print(thisdict[x])

# You can also use the values() function to return values of a dictionary:
for x in thisdict.values():
    print(x)

# Loop through both keys and values, by using the items() function:
for x, y in thisdict.items():
    print(x, y)

# Check if Key Exists:
if "name" in thisdict:
    print("Yes, 'Name' is one of the keys in the thisdict dictionary")

    # Adding an item to the dictionary is done by using a new index key and assigning a value to it:
    thisdict["result"] = "70%"
print(thisdict)

# There are several methods to remove items from a dictionary:
# 1--The pop() method removes the item with the specified key name:

thisdict.pop("roll_number")
print(thisdict)

# in versions before 3.7, a random item is removed instead:
thisdict.popitem()
print(thisdict)

# 2--The del keyword removes the item with the specified key name:
del thisdict["name"]
print(thisdict)

# use the dict() constructor to make a dictionary:
thisdict = dict(name="Alex", roll_number="3456667", passing_year=1964)
print(thisdict)
