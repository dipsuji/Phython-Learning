print("calculate the sum of a list of numbers.")


def array_sum(a):
    print(sum(a))


a = [2, 3, 5, 8]
array_sum(a)

print("calculate the value of 'a' to the power 'b'")


def power(a, b):
    """
    calculate the value of 'a' to the power 'b'
    :param a:
    :param b:
    :return:
    """
    return pow(a, b)


print(power(2, 2))
print(power(3, 4))

print("calculate the harmonic sum of n-1")


def harmonic_sum(n):
    """
    calculate the harmonic sum of n-1-----
    :param n:
    :return:
    """
    if n < 2:
        return 1
    else:
        return 1 / n + (harmonic_sum(n - 1))


print(harmonic_sum(2))
print(harmonic_sum(3))

print("calculate the geometric sum of n-1")


def geometric_sum(n):
    """
    calculate the geometric sum of n-1
    :param n:
    :return:
    """
    if n < 1:
        return 1
    else:
        return 1 / (pow(2, n)) + geometric_sum(n - 1)  # 1/4 + 1/2 + 1


print(geometric_sum(2))
print(geometric_sum(3))

print("calculate the sum of n")


def fun1(n):
    """
    sum up to n using recursion
    :param n:
    :return:
    """
    if n == 0:
        return 0
    else:
        return n + fun1(n - 1)


print(fun1(5))

print("calculate the sum of log n base 2 ")

import math


def fun2(n):
    """
    calculate the sum of log n base 2
    :param n:
    :return:
    """
    if n == 1:
        return 0
    else:
        return math.log(n, 2) + fun2(n - 1)


print(fun2(4))

print("find gratest common factor")


def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x


print(gcd(32, 16))

print("find greatest common factor using recursion")


def gcd_recursive(a, b):
    if b == 0:
        return a
    else:
        return gcd_recursive(b, a % b)


print(gcd_recursive(100, 24))
