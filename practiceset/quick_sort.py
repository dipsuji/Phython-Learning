def partition(arr, first, last):
    """
    The main function that implements QuickSort
    arr[] --> Array to be sorted,
    low  --> Starting index,
    high  --> Ending index
    :param arr:
    :param first:
    :param last:
    :return:
    """
    i = (first - 1)  # index of smaller element
    pivot = arr[last]  # pivot

    for j in range(first, last):

        # If current element is smaller than or
        # equal to pivot
        if arr[j] <= pivot:
            # increment index of smaller element
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[last] = arr[last], arr[i + 1]
    return i + 1


# Function to do Quick sort

def quick_Sort(arr, low, high):
    if low < high:
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr, low, high)

        # Separately sort elements before
        # partition and after partition
        quick_Sort(arr, low, pi - 1)
        quick_Sort(arr, pi + 1, high)

    # Driver code to test above


arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quick_Sort(arr, 0, n - 1)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i])
