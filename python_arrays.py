# Hello World program in Python

print("Python Arrays")
# Arrays are used to store multiple values in one single variable:
# Create an array containing country names:

countries = ["America", "India", "Japan"]

# Access the Elements of an Array
x = countries[0]
print(x)

# Modify the value of the first array item:
countries[0] = "China"
print(countries)

# Return the number of elements in the cars array:
x = len(countries)
print(x)

# Looping Array Elements
for x in countries:
    print(x)

# Adding Array Elements
# You can use the append() method to add an element to an array.
countries.append("Africa")
print(countries)

# Removing Array Elements
# You can use the pop() method to remove an element from the array.
countries.pop(1)
print(countries)

# You can also use the remove() method to remove an element from the array.
countries.remove("Japan")
print(countries)