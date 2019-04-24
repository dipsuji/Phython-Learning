def fraction_plusMinus(arr):
    count_pos = 0
    count_neg = 0
    count_0 = 0
    arr_len = len(arr)
    # print(arr_len)

    # print(arr)
    for i in range(0, len(arr)):
        if arr[i] > 0:
            count_pos += 1

        elif arr[i] < 0:
            count_neg += 1

        elif arr[i] == 0:
            count_0 += 1

    propor_pos = round(count_pos / arr_len, arr_len)
    propor_neg = round(count_neg / arr_len, arr_len)
    propor_zero = round(count_0 / arr_len, arr_len)

    # print(propor_pos, propor_neg, propor_zero, sep=' ', end='\n')
    print(propor_pos, end='\n')
    print(propor_neg, end='\n')
    print(propor_zero, end='\n')
fraction_plusMinus([-2, 3, -4, 0, 5, 1])

fraction_plusMinus([5, 2, -4, 0, 0, 1, -3])
