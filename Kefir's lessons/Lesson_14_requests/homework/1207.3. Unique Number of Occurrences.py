from collections import Counter


arr = [1,2,2,1,1,3]


def f(arr):
    d = Counter(arr)
    return len(set(d.values())) == len(d)

print(f(arr))
