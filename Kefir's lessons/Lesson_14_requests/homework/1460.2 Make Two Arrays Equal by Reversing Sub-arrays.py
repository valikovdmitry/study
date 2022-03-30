target = [1,2,3,4]
arr = [2,4,1,3]


def canBeEqual(target, arr):

    return sorted(arr) == sorted(target)

print(canBeEqual(target, arr))

