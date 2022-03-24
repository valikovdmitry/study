



l = [1,2,2,3]
d = dict()


def repeatedNTimes(nums):
    for value in nums:
        d[value] = d.get(value, 0) + 1
        if d.get(value) > 1:
            return value

print(repeatedNTimes(l))