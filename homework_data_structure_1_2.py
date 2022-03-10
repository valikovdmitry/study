# 1. выведи все функции из массива значение которых по модулю 5 < 2

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
lst2 = []
for i in range(21, 41):
    lst2.append(i)



def find(s, y=5):
    print('\n', s, sep='')
    for value in s:
        x = value % y
        if x < 2:
            print('\t', value, '- значение по модулю', y, ':', x)

find(lst)
find(lst2)










