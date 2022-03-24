





arr = [1,2,2,1,1,3]

def f(arr):
    d = dict()
    for value in arr:
        d[value] = d.get(value, 0) + 1

    res = []
    for v in d.values():
        res.append(v)

    return len(res) == len(set(res))

print(f(arr))