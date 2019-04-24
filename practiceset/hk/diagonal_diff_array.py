def diagonalDiff(arr):
    # Initialize sums of diagonals
    sumd1 = 0
    sumd2 = 0

    for i in range(0, len(arr)):

        for j in range(0, len(arr)):

            # finding sum of primary diagonal - arr[1][1]+arr[2][2]+arr[3]a[3]....
            if (i == j):
                sumd1 += arr[i][j]

                # finding sum of secondary diagonal -
            if (i == len(arr) - j - 1):
                sumd2 += arr[i][j]

                # Absolute difference of the sums
    return abs(sumd1 - sumd2);

print(diagonalDiff([[15, 2, 4], [4, 5, 6], [10, 8, -12]]))
print(diagonalDiff([[12, 2, 4], [4, 15, 6], [10, 8, 16]]))
