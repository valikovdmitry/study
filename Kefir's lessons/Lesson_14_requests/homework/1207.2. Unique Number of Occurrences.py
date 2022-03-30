arr = [1,2,2,1,1,3]


def f(arr):
    d = dict()
    for value in arr:
        d[value] = d.get(value, 0) + 1

    return len(set(d.values())) == len(d)

print(f(arr))
