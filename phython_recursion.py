import sys

sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())

i = 0


def greet():
    global i
    i += 1
    print("Hello", i)
    greet()


greet()


def fact(n):
    if n == 0:
        return 1

    return n * fact(n - 1)


result = fact(5)
print(result)
