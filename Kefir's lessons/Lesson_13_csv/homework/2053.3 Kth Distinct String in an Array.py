from collections import Counter

arr = ["d","b","c","b","c","a"]
k = 2

def kthDistinct(arr, k):
    d = Counter(arr)
    for key, v in d.items():
        if v == 1:
            k -= 1
            if k == 0:
                return key

    return ''

print(kthDistinct(arr, k))



