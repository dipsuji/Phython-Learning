def count_largest_num(ar):
    count_tallest = 0
    # print(max(ar))
    mx = max(ar)
    for i in range(0, len(ar)):
        # print(ar[i])
        if ar[i] == mx:
            count_tallest += 1
            # print(count_tallest)
    print(count_tallest)


count_largest_num([3, 5, 6, 4, 3, 6, 2, 6])
