from collections import Counter


lst = [3,2,3,2,2,2]


def divideArray(nums):
    d = Counter(nums)
    print(d)

    for value in d.values():
        if value % 2 != 0:
            return False
    return True

print(divideArray(lst))
