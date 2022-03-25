nums1 = [1,1,3,2]
nums2 = [2,3]
nums3 = [3]


def twoOutOfThree(nums1, nums2, nums3):
    d = dict()
    # доделать самому
    for num in nums1:
        d[num] = 1
    for num in set(nums2):
        d[num] = d.get(num, 0) + 1
    for num in set(nums3):
        d[num] = d.get(num, 0) + 1

    return [k for k, v in d.items() if v > 1]



print(twoOutOfThree(nums1, nums2, nums3))