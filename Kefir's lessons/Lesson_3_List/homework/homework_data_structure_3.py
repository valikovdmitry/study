# 3. Функция которая находит индекс максимального числа

lst = [1, 2, 3, 4, 12, 5, 6, 7, 17, 9]
lst2 = []
for i in range(21, 41):
    lst2.append(i)


def findmax(x):
    print('\nСамое большое число: ', max(x), '.', sep='')
    print('Оно находится на', x.index(max(x)), 'месте в массиве.')

findmax(lst)
findmax(lst2)











