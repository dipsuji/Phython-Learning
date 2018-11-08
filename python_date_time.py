# Hello World program in Python

print("Example of Python Date  Time")
# Python Dates
# A date in Python is not a data type of its own, but we can import a module named datetime to work with dates as date objects.
# The date contains year, month, day, hour, minute, second, and microsecond.
import datetime

x = datetime.datetime.now()
print(x)

# Date Output--
# The datetime module has many methods to return information about the date object.
# Here are a few examples, you will learn more about them later in this chapter:

print("Return the year and name of weekday:")
import datetime

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))

# Create a date object:

import datetime

x = datetime.datetime(2020, 5, 17)

print(x)

# The strftime() Method-----
# The datetime object has a method for formatting date objects into readable strings.
# The method is called strftime(), and takes one parameter, format, to specify the format of the returned string:

import datetime

x = datetime.datetime(2018, 6, 1)

print(x.strftime("%B"))

print(" A reference of all the legal format codes:---")

print(x.strftime("%a"))     # Weekday, short version-- thu

print(x.strftime("%A"))     # Weekday, full version-- thursday

print(x.strftime("%w"))     # Weekday as a number 0-6, 0 is Sunday-

print(x.strftime("%d"))     # Day of month 01-31

print(x.strftime("%b"))     # Month name, short version

print(x.strftime("%B"))     # Month name, full version

print(x.strftime("%m"))     # Month as a number 01-12

print(x.strftime("%y"))     # Year, short version, without century

print(x.strftime("%Y"))     # Year, full version

print(x.strftime("%H"))     # Hour 00-23

print(x.strftime("%I"))     # Hour 00-12

print(x.strftime("%p"))     # AM/PM

print(x.strftime("%M"))     # Minute 00-59

print(x.strftime("%S"))     # Second 00-59

print(x.strftime("%f"))     # Microsecond 000000-999999

print(x.strftime("%z"))     # UTC offset

print(x.strftime("%Z"))     # Timezone

print(x.strftime("%j"))     # Day number of year 001-366

print(x.strftime("%W"))     # Week number of year, Monday as the first day of week, 00-53

print(x.strftime("%U"))     # Week number of year, Sunday as the first day of week, 00-53

print(x.strftime("%c"))     # Local version of date and time

print(x.strftime("%X"))     # Local version of date

print(x.strftime("%x"))     # Local version of time

print(x.strftime("%%"))     # A % character
