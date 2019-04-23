def count_pairs(ar):
    count = 0
    result = {}
    for st in ar:
        if st not in result:
            result[st] = 1
        else:
            result[st] = result[st] + 1
    for value in result.values():
        count += int(value / 2)

    return count

print(count_pairs([22,10,10,20,20,30,50,30]))
print(count_pairs([22,10,10,20,20,30,50,30, 22, 10]))