nums = [8,1,2,2,3]
nums2 = [6,5,4,8]
nums3 = [7,7,7,7]


def func(x):
    count = 0
    result = []
    for orig in x:
        for value in x:
            if value < orig:
                count += 1
        result.append(count)
        count = 0
    return result

print(func(nums))


# n ** 2