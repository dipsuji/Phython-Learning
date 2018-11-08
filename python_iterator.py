# Hello World program in Python

print("Example of Python Iterators")
# An iterator is an object that contains a countable number of values.
# Lists, tuples, dictionaries, and sets are all iterable objects.
#  They are iterable containers which you can get an iterator from.
# Return a iterator from a tuple, and print each value:

mytuple = ("India", "Africa", "Japan")
myiter = iter(mytuple)

print(next(myiter))
print(next(myiter))
print(next(myiter))

# Strings are also iterable objects, containing a sequence of characters:
mystr = "Africa"
myiter = iter(mystr)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

# Looping Through an Iterator
for x in mytuple:
    print(x)

print("Create an iterator")


# Create an iterator that returns numbers, starting with 1, and each sequence will increase by one (returning 1,2,3,4,5 etc.):

class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x


myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

print("StopIteration")


# The example above would continue forever if you had enough next() statements, or if it was used in a for loop.
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 10:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
    print(x)
