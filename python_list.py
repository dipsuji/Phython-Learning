# Hello World program in Python

print("Example of Python Lists\n")
# In Python lists are written with square brackets.

thislist = ["apple", "banana", "cherry"]
print(thislist)

# You access the list items by referring to the index number:
print(thislist[1])

# To change the value of a specific item, refer to the index number:
thislist[1] = "blackcurrant"
print(thislist)

# You can loop through the list items by using a for loop:
# Print all items in the list, one by one:

for x in thislist:
    print(x)

# To determine if a specified item is present in a list use the in keyword:
# Check if "apple" is present in the list:

if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")
print(x)

# To determine how many items a list have, use the len() method:
# Print the number of items in the list:

print(len(thislist))
print(x)

# To add an item to the end of the list, use the append() method:
# Using the append() method to append an item:

thislist.append("orange")
print(thislist)

# To add an item at the specified index, use the insert() method:
# Insert an item as the second position:

thislist.insert(1, "orange")
print(thislist)

# The remove() method removes the specified item:

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

# The pop() method removes the specified index, (or the last item if index is not specified):

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

# The del keyword removes the specified index:

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

# Using the list() constructor to make a List:

thislist = list(("apple", "banana", "cherry"))  # note the double round-brackets
print(thislist)
