# code

def solve(num):
    count = 0
    num = str(num)
    revNum = int(num[::-1])
    nextNum = int(num) + revNum
    count += 1
    if (count > 5):
        return -1
    if poli:
        return nextNum
    else:
        return solve(nextNum)


def poli(nextNum):
    if nextNum == int(str(nextNum)[::-1]):
        return True
    else:
        return False


test = int(input())
for t in range(0, test):

    print(solve(int(input())))


solve(667)


def squirrel_play(temp, is_summer):
    if is_summer is True:
        if temp >=60 or temp <=90:
            return True
        return False
    else:
        if temp >= 60 or temp <= 100:
            return True
        return False