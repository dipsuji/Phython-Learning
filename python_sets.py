# Hello World program in Python

print("Python Sets\n")
thisset = {"Alex", "James", "Sora"}
print(thisset)

# Loop through the set, and print the values:
for x in thisset:
    print(x)

    # Check if "banana" is present in the set:
    thisset = {"Alex", "James", "Sora"}
    print("James" in thisset)

    # nce a set is created, you cannot change its items, but you can add new items.
    # Add an item to a set, using the add() method:
    thisset.add("Aadit")

print(thisset)

# Add multiple items to a set, using the update() method:
thisset.update(["Alexi", "Promi", "Abrahm"])

print(thisset)

# determine how many items a set have, use the len() method.

print(len(thisset))

# remove an item in a set, use the remove(), or the discard() method.

thisset.remove("Alex")

print(thisset)

# Remove the last item by using the pop() method:

x = thisset.pop()

print(x)

print(thisset)

# The clear() method empties the set:

thisset.clear()

print(thisset)

# The del keyword will delete the set completely:
# this will raise an error because the set no longer exists

r = {"Alex", "James", "Sora"}

del r
