target = [1,2,3,4]
arr = [2,4,1,3]

def canBeEqual(target, arr):
    sort_target = sorted(target)
    print(sort_target)
    sort_arr = sorted(arr)
    print(sort_arr)


    return sort_arr == sort_target

print(canBeEqual(target, arr))
