nums = [5,3,6,1,12]
original = 3

nums2 = [8,19,4,2,15,3]
original2 = 2


def findFinalValue(nums, original):
    nums_set = set(nums)
    while original in nums_set:
        original *= 2
    return original

print(findFinalValue(nums, original))
print(findFinalValue(nums2, original2))




