lst = [3,2,3,2,2,2]


def divideArray(nums):
    d = dict()
    for value in nums:
        d[value] = d.get(value, 0) + 1
    print(d)

    for value in d.values():
        if value % 2 != 0:
            return False
    return True

print(divideArray(lst))
