# Hello World program in Python

print("Python JSON")

# JSON is a syntax for storing and exchanging data.
# JSON is text, written with JavaScript object notation.

print("Parse JSON - Convert from JSON to Python")
import json

# some JSON:
x = '{ "name":"Alex", "age":40, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])

print("Convert from Python to JSON")

# If you have a Python object, you can convert it into a JSON string by using the json.dumps() method.
# a Python object (dict):
x = {
    "name": "Alex",
    "age": 40,
    "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)

# You can convert Python objects of the following types, into JSON strings:
# dict
# list
# tuple
# string
# int
# float
# True
# False
# None

print("Some example to Convert Python objects into JSON strings, and print the values:")
print(json.dumps({"name": "Alex", "age": 40}))
print(json.dumps(["India", "Japan"]))
print(json.dumps(("India", "Japan")))
print(json.dumps("hello,good morning"))
print(json.dumps(48))
print(json.dumps(31.56))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

print("Convert a Python object containing all the legal data types:")
x = {
    "name": "Alex",
    "age": 40,
    "married": True,
    "divorced": False,
    "children": ("Anna", "Giselle"),
    "pets": None,
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
    ]
}

print(json.dumps(x))
# The example above prints a JSON string, but it is not very easy to read, with no indentations and line breaks.
# use four indents to make it easier to read the result:
print("Use the indent parameter to define the numbers of indents:")

print(json.dumps(x, indent=4))

# You can also define the separators, default value is (", ", ": "),
# which means using a comma and a space to separate each object, and a colon and a space to separate keys from values:
print("Use the separators:")
# # use . and a space to separate objects, and a space, a = and a space to separate keys from their values:
print(json.dumps(x, indent=4, separators=(". ", " = ")))

# Use the sort_keys parameter to specify if the result should be sorted or not:
print("sort the result alphabetically by keys:")
print(json.dumps(x, indent=4, sort_keys=True))
