def second_largest1(number):
    n = len(number)
    number.sort()
    print("Second largest element is:", number[n - 2])


second_largest1([20, 67, 3, 2.6, 7, 74, 2.8, 90.8, 52.8, 4, 3, 2, 5, 7])


def second_largest(numbers):
    count = 0
    largest = second_largest = float('-inf')
    print(largest)
    for num in numbers:
        count += 1
        if num > second_largest:
            if num >= largest:
                largest, second_largest = num, largest
                print(largest, second_largest)
            else:
                second_largest = num
    return second_largest if count >= 2 else None


print("second largest no. is: ", second_largest([20, 67, 3, 2.6, 7, 74, 2.8, 90.8, 52.8, 4, 3, 2, 5, 7]))


def getPairsCount(arr, sum):
    n = len(arr)

    # Consider all possible pairs
    # and check their sums
    for i in range(0, n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == sum:
                print("pair is", "(", arr[i],
                      ", ", arr[j],
                      ")", sep="")


# Driver function
arr = [1, 5, 7, -1, 6, 0, 3, 3]
sum = 6
getPairsCount(arr, sum)
