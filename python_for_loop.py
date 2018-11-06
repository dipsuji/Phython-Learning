# Hello World program in Python
print("Example Python For Loops")
# Print each country in a country list:
countries = ["India", "America", "Japan", "China", "Africa"]
for x in countries:
    print(x)

print("Example Looping Through a String")
# Even strings are iterable objects, they contain a sequence of characters:
for x in "Japan":
    print(x)

print("Example The break Statement")
# With the break statement we can stop the loop before it has looped through all the items:
for x in countries:
    print(x)
    if x == "America":
        break
print("Example of The continue Statement")
# With the continue statement we can stop the current iteration of the loop, and continue with the next:
for x in countries:
    if x == "America":
        continue
    print(x)

print("Using the Range () function")
# The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default),
# and ends at a specified number:
for x in range(5):
    print(x)
print("Using the start parameter:")
#  it is possible to specify the starting value by adding a parameter:
for x in range(1, 6):
    print(x)

# The range() function defaults to increment the sequence by 1, however
# it is possible to specify the increment value by adding a third parameter:
for x in range(2, 15, 3):
    print(x)

print("Else in For Loop")
# The else keyword in a for loop specifies a block of code to be executed when the loop is finished:
for x in range(5):
    print(x)
else:
    print(" finished!")

print("Nested Loops")
# A nested loop is a loop inside a loop:
adj = ["big", "technical", "traditional"]
countries = ["India", "America", "Japan", "China", "Africa"]

for x in adj:
    for y in countries:
        print(x, y)

print("Recursion Example")


def tri_recursion(k):
    if (k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result


print("\n\nRecursion Example Results")
tri_recursion(6)
