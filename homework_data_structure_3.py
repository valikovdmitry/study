# 3. Функция которая находит индекс максимального числа

lst = [1, 2, 3, 4, 12, 5, 6, 7, 17, 9]


result = []

def findmax(x):
    print('Самое большое число:', max(x), '.')
    print('Оно находится на', x.index(max(x)), 'месте в массиве.')

findmax(lst)