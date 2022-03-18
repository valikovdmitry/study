nums = [0, 2, 3, 4]
ans = []

k = 2
while k != 0:
    for value in nums:
        ans.append(value)
    k -= 1

print(ans)
