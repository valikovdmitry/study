





nums1 = [1,1,3,2]
nums2 = [2,3]
nums3 = [3]


def twoOutOfThree(nums1, nums2, nums3):
    set1 = set(nums1)
    set2 = set(nums2)
    set3 = set(nums3)

    inter1 = set1.intersection(set2)
    inter2 = set2.intersection(set3)
    inter3 = set3.intersection(set1)

    all = []
    for v in nums1:
        if v not in all:
            all.append(v)
    for v in nums2:
        if v not in all:
            all.append(v)
    for v in nums3:
        if v not in all:
            all.append(v)

    selected = []
    for v in all:
        if v in inter1 or v in inter2 or v in inter3:
            selected.append(v)

    return selected


print(twoOutOfThree(nums1, nums2, nums3))