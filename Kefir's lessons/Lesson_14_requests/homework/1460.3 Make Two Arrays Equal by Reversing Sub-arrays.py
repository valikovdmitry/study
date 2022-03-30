from collections import Counter

target = [1,2,3,4]
arr = [2,4,1,3]


def canBeEqual(target, arr):

    print(Counter(target))
    print(Counter(arr))
    return Counter(target) == Counter(arr)

print(canBeEqual(target, arr))

