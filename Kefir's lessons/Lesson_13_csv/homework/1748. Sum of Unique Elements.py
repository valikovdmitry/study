



lst = [1,2,3,2]

def sumOfUnique(nums):
    d = dict()
    for value in nums:
        d[value] = d.get(value, 0) + 1

    result = []
    for key, value in d.items():
        if value == 1:
            result.append(key)

    return sum(result)

print(sumOfUnique(lst))
