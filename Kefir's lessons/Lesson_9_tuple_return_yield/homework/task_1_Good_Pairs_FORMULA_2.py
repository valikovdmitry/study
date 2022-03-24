input3 = [1, 2, 3, 1, 1, 3]
input1 = [1, 1, 1, 1]
input2 = [1, 2, 3]


def good_pairs(x):
    formula = int((x * (x - 1)) / 2)
    return formula

d = dict()

# for num in input3:
#     if num not in d:
#         d[num] = 0
#     d[num] += 1
#
# print(d)


for num in input3:
    d[num] = d.get(num, 0) + 1
print(d)

result_count = 0
for num, count in d.items():
    result_count += good_pairs(count)
print(result_count)