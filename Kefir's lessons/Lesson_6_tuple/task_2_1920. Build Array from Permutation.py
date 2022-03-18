nums = [0, 2, 1, 5, 3, 4]
primer = [0, 1, 2, 4, 5, 3]

nums2 = [5, 0, 1, 2, 3, 4]
primer2 = [4, 5, 0, 1, 2, 3]


def array(lst):
    result = []
    for value in lst:
        result.append(lst[value])
    print(lst)
    print(result, '\n')


array(nums)
array(nums2)

