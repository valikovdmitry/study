



str = "abacbc"

def areOccurrencesEqual(s):
    d = dict()
    for value in s:
        d[value] = d.get(value, 0) + 1
    print(d)

    check = []
    for value in d.values():
        check.append(value)

    count = 0
    for index, value in enumerate(check):
        prev = check[index - 1]
        if value == prev:
            count = count
        else:
            count += 1

    return count == 0

print(areOccurrencesEqual(str))