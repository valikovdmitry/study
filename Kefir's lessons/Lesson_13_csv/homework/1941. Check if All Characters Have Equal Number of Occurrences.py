str = "abacbc"

def areOccurrencesEqual(s):
    d = dict()
    for value in s:
        d[value] = d.get(value, 0) + 1

    return len(set(d.values())) == 1

print(areOccurrencesEqual(str))