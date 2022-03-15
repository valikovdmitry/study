nums = [8,1,2,2,3]
nums2 = [6,5,4,8]
nums3 = [7,7,7,7]


def func(x):
    res = []
    result = []
    index = 0
    while index < len(x):
        for value in x:
            if value < x[index]:
                res.append(value)
        result.append(len(res))
        res.clear()
        index += 1
    print(result)

func(nums)
func(nums2)
func(nums3)