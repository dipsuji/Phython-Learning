# Hello World program in Python

print("Python Classes and Objects")


# Create a Class
# To create a class, use the keyword class:

class MyClass:
    x = 5


print(MyClass)


# Create Object
# Now we can use the class named myClass to create objects:

class MyClass:
    x = 5


p1 = MyClass()
print(p1.x)


# The __init__() Function
# Create a class named Person, use the __init__() function to assign values for name and age:
#
class Person:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary


p1 = Person("Alex", 36, 400000)

print(p1.name)
print(p1.age)
print(p1.salary)


# Object Methods
# Objects can also contain methods. Methods in objects are functions that belongs to the object.
# Let us create a method in the Person class:

class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def myfunc(self):
        print("Hello my name is " + self.name)


p1 = Employee("John", 36, 500000)
p1.myfunc()


# The self Parameter
# The self parameter is a reference to the class itself, and is used to access variables that belongs to the class.
# It does not have to be named self ,
# you can call it whatever you like, but it has to be the first parameter of any function in the class:
class Person:
    def __init__(mysillyobject, name, age, salary):
        mysillyobject.name = name
        mysillyobject.age = age
        mysillyobject.salary = salary

    def myfunc(abc):
        print("Hello my name is " + abc.name)


p1 = Person("John", 36, 456000)
p1.myfunc()

# Modify Object Properties
# You can modify properties on objects like this:

p1.age = 40

print(p1.age)

# Delete Object Properties
# You can delete properties on objects by using the del keyword:

del p1.age

print(p1.age)
