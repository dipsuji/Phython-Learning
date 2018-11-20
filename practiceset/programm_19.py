def table(num):
    """
    find the table of given number
    :param num:
    :return:
    """

    for i in range(1, 11):
        print(num, 'x', i, '=', num * i)


table(12)


def find_power(x, y):
    """
    Write a program to find x to power y

    :param a:
    :param b:
    :return:
    """

    print(pow(x, y))


find_power(2, 4)


def power(base, exp):
    """
    Write a program to find x to power y using recursion
    :param base:
    :param exp:
    :return:
    """
    if exp == 0:
        return 1
    if exp != 0:
        return base * power(base, exp - 1)


print("Result:", power(3, 4))


def swap(first_num, second_num):
    """
    Write a program to swap two numbers without using third variable

    :param num:
    :return:
    """
    first_num = first_num + second_num
    second_num = first_num - second_num
    first_num = first_num - second_num
    print("firstnum:", first_num, " second_num:", second_num)


swap(1, 2)
