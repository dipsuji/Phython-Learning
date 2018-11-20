print("find Armstrong number in given range")


def armstrong_number(range_value):
    """
    find given no is Armstrong or not
    -->number of n digit which are equal to the sum of nth power of its digit----called Armstrong number

    :param range_value:
    :return:
    """
    for i in range(range_value):
        num = i
        result = 0
        n = len(str(i))
        while i != 0:
            digit = i % 10
            result = result + digit ** n
            # // return
            i = i // 10
        if num == result:
            print(num)


armstrong_number(10000)
