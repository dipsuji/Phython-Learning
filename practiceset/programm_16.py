def largest_num(num1, num2, num3):
    """
    find the largest number into the given list
    :param num1:
    :param num2:
    :param num3:
    :return:
    """
    # max = max(num1, num2,num3)
    # print(max)
    if (num1 >= num2) and (num1 >= num3):
        largest = num1
    elif (num2 >= num1) and (num2 >= num3):
        largest = num2
    else:
        largest = num3

    print("The largest number between", num1, ",", num2, "and", num3, "is: ", largest)


largest_num(10, 14, 12)


def decimal_to_binary(number):
    """
    convert decimal to binary of a given no.
    :param number:
    :return:
    """
    print("Equivalent Binary Number: ", bin(number))


decimal_to_binary(42)


def leap_year(year):
    """
    finding which year is a leap year
    :param year:
    :return:
    """
    if (year % 4) == 0:
        print("{0} is a leap year".format(year))
    else:
        print("{0} is not a leap year".format(year))


leap_year(2040)


def lower_case(string):
    print(string.lower())


lower_case("This Sh0uLd BE IN L0wErCasE!")


# Program make a simple calculator that can add, subtract, multiply and divide using functions

# This function adds two numbers
def add(x, y):
    return x + y


# This function subtracts two numbers
def subtract(x, y):
    return x - y


# This function multiplies two numbers
def multiply(x, y):
    return x * y


# This function divides two numbers
def divide(x, y):
    return x / y


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")


def simple_calculator(num1, num2, operation):
    if operation == 'add':
        print(num1, "+", num2, "=", add(num1, num2))

    elif operation == 'subtract':
        print(num1, "-", num2, "=", subtract(num1, num2))

    elif operation == 'multiply':
        print(num1, "*", num2, "=", multiply(num1, num2))

    elif operation == 'divide':
        print(num1, "/", num2, "=", divide(num1, num2))
    else:
        print("Invalid input")


simple_calculator(50, 10, 'subtract')


def check_palindrome(string):
    # make it suitable for caseless comparison
    print(string)
    string = string.casefold()
    print(string)
    # reverse the string
    rev_str = reversed(string)

    # check if the string is equal to its reverse
    if list(string) == list(rev_str):
        print("It is palindrome")
    else:
        print("It is not palindrome")


check_palindrome("MalayAlam")
