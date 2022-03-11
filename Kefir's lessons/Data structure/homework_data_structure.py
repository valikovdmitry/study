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




# 2. На входе список из любых типов переменных. Задача удалиить из списка все с типом str.

lst = [1, 0.5, 'sring', 2, 0.7, 'word', 7, 3.5, 'sea']
lst2 = [2, 1.5, 'star', 3, 8.7, 'work', 9, 4.5, 'tea']

def remove(x, y=str):
    print('\n', x)
    for value in x:
        if (isinstance(value, y)) == True:
            x.remove(value)
    print('\n \t After remove str:', '\n', '\t', x, '\n \n')

remove(lst)
remove(lst2)




# 3. Функция которая находит индекс максимального числа

lst = [1, 2, 3, 4, 12, 5, 6, 7, 17, 9]
lst2 = []
for i in range(21, 41):
    lst2.append(i)

result = []

def findmax(x):
    print('\nСамое большое число:', max(x), '.')
    print('Оно находится на', x.index(max(x)), 'месте в массиве.')

findmax(lst)
findmax(lst2)