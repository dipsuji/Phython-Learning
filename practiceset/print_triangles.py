def print_triangle_star(height):
    """
    print right triangle using star---
    :param height:
    :return:
    """
    for i in range(height, 0, -1):
        print(i * ' ' + (height + 1 - i) * '*')


print_triangle_star(5)


def print_triangle(height):
    """
    print triangle
    :param height:
    :return:
    """
    for i in range(0, height):
        for j in range(0, height - i - 1):
            print(end=" ")
        for j in range(0, i + 1):
            print("*", end=" ")
        print()


print_triangle(4)


def pyramid(rows):
    for i in range(rows):
        print('' * (rows - i - 1) + '*' * (2 * i + 1))


pyramid(4)


def pyramid_inverted(rows):
    """
    print inverted triangle ----
    :param rows:
    :return:
    """
    for i in range(rows, 0, -1):
        for j in range(0, i):
            print("*", end=" ")
        print()


pyramid_inverted(6)
