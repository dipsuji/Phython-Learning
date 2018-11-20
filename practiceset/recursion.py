# calling function inside function

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


f = factorial(5)
print(f)
