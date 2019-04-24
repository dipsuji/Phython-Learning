import array

# initializing array with array values
# initializes array with signed integers
arr = array.array('i', [1, 2, 3])

# printing original array
print("The new created array is : ", end=" ")
for i in range(0, 3):
    print(arr[i], end=" ")

print("\r")

# using append() to insert new value at end
arr.append(4);
print(arr)
# printing appended array
print("The appended array is : ", end="")
for i in range(0, 4):
    print(arr[i], end=" ")

# using insert() to insert value at specific position
# inserts 5 at 2nd position
arr.insert(2, 5)

print("\r")

# printing array after insertion
print("The array after insertion is : ", end="")
for i in range(0, 5):
    print(arr[i], end=" ")

print("\r")

print("The popped element is : ", end="")
print(arr.pop(2))

# printing array after popping
print("The array after popping is : ", end="")
for i in range(0, 4):
    print(arr[i], end=" ")

print("\r")

# using remove() to remove 1st occurrence of 1
arr.remove(1)

# printing array after removing
print("The array after removing is : ", end="")
for i in range(0, 3):
    print(arr[i], end=" ")

print("\r")

print("The index of 1st occurrence of 2 is : ", end="")
print(arr.index(2))

# using reverse() to reverse the array
arr.reverse()

# printing array after reversing
print("The array after reversing is : ", end="")
for i in range(0, 3):
    print(arr[i], end=" ")

