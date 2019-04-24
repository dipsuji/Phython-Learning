def solve(len1, ar, s):
    for i in range(0, len1 - 3):
        # Fix the second element and
        # find other two
        for j in range(i + 1, len1 - 2):

            # Fix the third element
            # and find the fourth
            for k in range(j + 1, len1 - 1):

                # find the fourth
                for l in range(k + 1, len1):
                    if ar[i] + ar[j] + ar[k] + ar[l] == s:
                        return 1
    return 0

test = int(1)
for t in range(0, test):
    ar = [1, 5, 1, 0, 6, 0]
    print(solve(6, ar, 7))
