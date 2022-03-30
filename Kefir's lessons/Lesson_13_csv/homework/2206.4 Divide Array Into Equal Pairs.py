from collections import Counter


lst = [3,2,3,2,2,2]


def divideArray(nums):
    len_ = len(nums)//2
    sum_ = sum(value//2 for value in Counter(nums).values())

    return sum_ == len_

print(divideArray(lst))
