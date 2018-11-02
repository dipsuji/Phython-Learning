# Hello World program in Python
print("Example of Python Tuples\n")
# Create a Tuple:

thistuple = ("apple", "banana", "cherry")
print(thistuple)

# You can access tuple items by referring to the index number:
# Return the item in position 1:

print(thistuple[1])

# You can loop through the tuple items by using a for loop.
# Iterate through the items and print the values:

for x in thistuple:
    print(x)

    # To determine if a specified item is present in a tuple use the in keyword:
# Check if "apple" is present in the tuple:

thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
    print("Yes, 'apple' is in the fruits tuple")

# To determine how many items a list have, use the len() method:
# Print the number of items in the tuple:

print(len(thistuple))

# Using the tuple() method to make a tuple:

thistuple = tuple(("apple", "banana", "cherry"))  # note the double round-brackets
print(thistuple)

# Once a tuple is created, you cannot add items to it. Tuples are unchangeable.
# You cannot add items to a tuple:

thistuple = ("apple", "banana", "cherry")
thistuple[3] = "orange"  # This will raise an error
print(thistuple)

# The del keyword can delete the tuple completely:

del thistuple
print(thistuple)  # this will raise an error because the tuple no longer exists
