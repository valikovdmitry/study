lst = [1,2,3,4,5,6,7,8,9] * 10

res = [1]
stop = 1
index = 1
while len(res) < 9:
    s = lst[index] + res[-1]
    if s % 3 != 0 and s % 5 != 0 and s % 7 != 0:
        res.append(lst[index])
        index = 0

    index += 1
    stop += 1
print(res)