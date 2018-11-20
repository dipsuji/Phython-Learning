pos = -1


def search(list, n):
    """
    search using binary---
    The idea of binary search is to use the information that the array is sorted and reduce the time complexity

    :param list:
    :param n:
    :return:
    """
    l = 0
    u = len(list) - 1
    while l <= u:
        mid = (l + u) // 2

        if list[mid] == n:
            globals()['pos'] = mid
            return True
        else:
            if list[mid] < n:
                l = mid + 1
            else:
                u = mid - 1
    return False


8

list = [4, 7, 7, 35, 100]
n = 10

if search(list, n):
    print("find at position ", pos + 1)
else:
    print("not find")
