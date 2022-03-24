lst = [1,2,3,4,5,6,7,8,9]
d = {1: [3, 7], 2: [6, 9], 3: [1, 5, 8], 4: [7, 9], 5: [3, 6, 8], 6: [2, 5, 7], 7: [1, 4, 6, 9], 8: [3, 5, 9], 9: [2, 4, 7, 8]}

result = []
while len(result) < 9:
    index = 0
    result.append(lst[0])



first = 1                   # взял первое число
for value in d.values():
    if 1 in value:
        value.remove(1)     # удалил это число из возможных потому что уже использовал его
print(first)

res = d[1][0]               # взял певрое значие по ключу - 1 (это 3)
for value in d.values():
    if 3 in value:
        value.remove(3)     # удалил 3 - уже использовал его
print(res)

next = d[res][0]            # взял певрое значие по ключу - 3 (это 5)
for value in d.values():
    if 5 in value:
        value.remove(5)     # удалил 5 - уже использовал его
print(next)

next2 = d[next][0]          # взял певрое значие по ключу - 5 (это 6)
for value in d.values():
    if 5 in value:          # удалил 6 - уже использовал его
        value.remove(5)
print(next2)




print(d)