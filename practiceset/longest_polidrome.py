def polindrom(str1):
    last = len(str1) - 1
    for i in range(0, int(len(str1) / 2)):
        if str1[i] != str1[last]:
            return False
        last = last - 1
    return True


print(polindrom("abcaba"))


def longestPalSubstr(string):
    maxLength = 1

    start = 0
    length = len(string)

    low = 0
    high = 0

    # One by one consider every character as center point of
    # even and length palindromes
    for i in range(1, length):
        # Find the longest even length palindrome with center
        # points as i-1 and i.
        low = i - 1
        high = i
        while low >= 0 and high < length and string[low] == string[high]:
            if high - low + 1 > maxLength:
                start = low
                maxLength = high - low + 1
            low -= 1
            high += 1

        # Find the longest odd length palindrome with center
        # point as i
        low = i - 1
        high = i + 1
        while low >= 0 and high < length and string[low] == string[high]:
            if high - low + 1 > maxLength:
                start = low
                maxLength = high - low + 1
            low -= 1
            high += 1

    print("Longest palindrome substring is:"),
    print(string[start:start + maxLength])

    return maxLength


# Driver program to test above functions
string = "hisingisignishi"
print("Length is: " + str(longestPalSubstr(string)))
