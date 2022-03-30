from collections import Counter

arr = ["d","b","c","b","c","a"]
k = 2

def kthDistinct(arr, k):
    arr_dict = Counter(arr)
    for key, value in arr_dict.items():
        if value == 1:
            k -= 1
            if not k:
                return key
    return ''

print(kthDistinct(arr, k))



