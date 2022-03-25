



lowLimit = 100
highLimit = 111

def countBalls(lowLimit, highLimit):
    d = dict()
    for value in range(lowLimit,highLimit + 1):
        box = sum(map(int, str(value)))
        d[box] = d.get(box, 0) + 1

    return max(d.values())

print(countBalls(lowLimit, highLimit))


