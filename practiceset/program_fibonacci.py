# Hello World program in Python
def fibonacci(num):
    """
    print fibonacci of a given no.
    :param num:
    :return:
    """
    n1 = 0
    n2 = 1
    count = 0
    # check if the number of terms is valid
    if num <= 0:
        print("Please enter a positive integer")
    elif num == 1:
        print("Fibonacci sequence upto", num, ":")
        print(n1)
    else:
        print("Fibonacci sequence upto", num, ":")
        while count < num:
            print(n1, end=', ')
            nth = n1 + n2
            # update values
            n1 = n2
            n2 = nth
            count += 1


fibonacci(10)
