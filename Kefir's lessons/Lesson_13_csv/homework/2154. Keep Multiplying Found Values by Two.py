nums = [5,3,6,1,12]
original = 3

nums2 = [8,19,4,2,15,3]
original2 = 2

def findFinalValue(nums, original):
    nums_sorted = sorted(nums)
    orig = original
    for value in nums_sorted:
        if value == orig:
            orig *= 2
            print(orig)
    return orig

# print(findFinalValue(nums, original))
print(findFinalValue(nums2, original2))




