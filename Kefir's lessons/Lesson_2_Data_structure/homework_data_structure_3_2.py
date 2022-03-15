# 3. Функция которая находит индекс максимального числа

lst = [1, 2, 3, 4, 12, 5, 6, 7, 17, 9]
lst2 = []
for i in range(21, 41):
    lst2.append(i)


def argmax(x):
    return x.index(max(x))

print(argmax(lst))



argmax1 = lambda x: x.index(max(x))

print(argmax1(lst))












