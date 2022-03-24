




lst = [3,2,3,2,2,2]
d = dict()


def divideArray(nums):
    for value in nums:
        d[value] = d.get(value, 0) + 1
    print(d)

    count = 0
    for value in d.values():
        if value % 2 != 0:
            count += 1
        else:
            continue

    return count == 0


print(divideArray(lst))