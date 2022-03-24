nums = [3, 8, 7, 5, 4, 6]
k = 2
sorted_nums = sorted(nums)
d = {1: [], 2: []}

for num in sorted_nums:
    if num % 2 == 0:
        d[2].append(num)
    else:
        d[1].append(num)


noeven = d[1]
even = d[2]


count = 0
for index, value in enumerate(noeven):
    if value - noeven[index - 1] == 2:
        count += 1


for index, value in enumerate(even):
    if value - even[index - 1] == 2:
        count += 1


