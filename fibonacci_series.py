# Now we come to implement the factorial in Python. It's as easy and elegant as the mathematical definition.


def fibi(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
        print(a)
    return a


result = fibi(6)
print(result)
