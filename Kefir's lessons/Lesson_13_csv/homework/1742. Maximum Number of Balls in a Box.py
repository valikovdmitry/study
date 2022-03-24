



lowLimit = 100
highLimit = 111

def countBalls(lowLimit, highLimit):
    d = dict()
    for value in range(lowLimit,highLimit + 1):
        count = 0
        value_str = str(value)
        for v in value_str:
            count += int(v)
        d[value] = count
    print(d)

    d2 = dict()
    for value in d.values():
        d2[value] = d2.get(value, 0) + 1
    print(d2)

    return max(d2.values())

print(countBalls(lowLimit, highLimit))


