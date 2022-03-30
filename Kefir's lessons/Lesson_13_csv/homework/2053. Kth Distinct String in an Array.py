arr = ["d","b","c","b","c","a"]
k = 2

def kthDistinct(arr, k):
    d = dict()
    for value in arr:
        d[value] = d.get(value, 0) + 1

    res = []
    for key, value in d.items():
        if value == 1:
            res.append(key)

    if len(res) < k:
        return ''
    else:
        return res[k - 1]


print(kthDistinct(arr, k))