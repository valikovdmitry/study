lst = [3,2,3,2,2,2]


def divideArray(nums):
    nums_set = set(nums)
    for value in nums_set:
        if nums.count(value) % 2 != 0:
            return False
    return True


print(divideArray(lst))
