print("add two matrix----")


def add_two_matrix(X, Y):
    """
    program to add_two_matrix
    :param X:
    :param Y:
    :return:
    """
    result = [[0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0]]
    for i in range(len(X)):
        # iterate through columns
        for j in range(len(X[0])):
            result[i][j] = X[i][j] + Y[i][j]

    for r in result:
        print(r)


add_two_matrix([[12, 7, 3, 5],
                [4, 5, 6, 5],
                [7, 8, 9, 7],
                [5, 7, 3, 2]], [[5, 8, 1, 8],
                                [6, 7, 3, 4],
                                [4, 5, 9, 3],
                                [6, 8, 9, 3]])

print("subtract two matrix----")


def subtract_two_matrix(X, Y):
    """
    subtract_two_matrix
    :param X:
    :param Y:
    :return:
    """
    result = [[0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0]]
    for i in range(len(X)):
        # iterate through columns
        for j in range(len(X[0])):
            result[i][j] = X[i][j] - Y[i][j]

    for r in result:
        print(r)


subtract_two_matrix([[12, 7, 3, 5],
                     [4, 5, 6, 5],
                     [7, 8, 9, 7],
                     [5, 7, 3, 2]], [[5, 8, 1, 8],
                                     [6, 7, 3, 4],
                                     [4, 5, 9, 3],
                                     [6, 8, 9, 3]])

print("multiply two matrix----")


def multiply_two_matrix(X, Y):
    """
    multiply_two_matrix
    :param X:
    :param Y:
    :return:
    """
    result = [[0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0]]
    for i in range(len(X)):
        # iterate through columns of Y
        for j in range(len(Y[0])):
            # iterate through rows of Y
            for k in range(len(Y)):
                result[i][j] += X[i][k] * Y[k][j]

    for r in result:
        print(r)


multiply_two_matrix([[12, 7, 3, 5],
                     [4, 5, 6, 5],
                     [7, 8, 9, 7],
                     [5, 7, 3, 2]], [[5, 8, 1, 8],
                                     [6, 7, 3, 4],
                                     [4, 5, 9, 3],
                                     [6, 8, 9, 3]])
