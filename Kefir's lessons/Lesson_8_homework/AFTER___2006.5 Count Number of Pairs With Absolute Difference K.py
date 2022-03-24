lst1 = [1, 2, 4, 5, 6, 7]; k1 = 2
lst2 = [3, 2, 1, 5, 4]; k2 = 2
lst3 = [1, 2, 2, 1]; k3 = 1


def count_k_pairs(nums, k):
    hash_ = dict()
    count = 0

    for exict in nums:
        hash_[exict] = 0

    for key in nums:
        hash_[key] += 1

    for key, value in hash_.items():
        ans = key - k
        count += value * hash_.get(ans, 0)

    return count







print(lst1)
print(count_k_pairs(lst1, k1))
print(lst2)
print(count_k_pairs(lst2, k2))
print(lst3)
print(count_k_pairs(lst3, k3))
