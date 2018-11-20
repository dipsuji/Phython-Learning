def prime_number(given_range):
    """
    Write a program to print all prime number in the given range.View

    :param given_range:
    :return:
    """
    for a in range(2, given_range + 1):
        k = 0
        for i in range(2, a // 2 + 1):
            if (a % i == 0):
                k = k + 1
        if (k <= 0):
            print(a)


prime_number(15)


def reverse_number(number1):
    """
    print given number in a reverse order
    :param number1:
    :return:
    """
    reverse = 0
    while number1 > 0:
        reminder = number1 % 10
        reverse = (reverse * 10) + reminder
        number1 = number1 // 10
    print("\n Reverse of entered number is = %d" % reverse)


reverse_number(1234)

# this is another way to find reverse number
number = 123
number = int(str(number)[::-1])
print(number)


def reverse_string(string):
    print("Reverse of the string is: ")
    print(string[::-1])


reverse_string("sujata")


def simple_interest(p, r, t):
    """
    calculate SIMPLE INTEREST ----
    :param p:
    :param r:
    :param t:
    :return:
    """
    SI = (p * r * t) / 100
    print("simple interest is: ", SI)


simple_interest(1000, 10, 2)
