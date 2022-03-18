# допустин
#
# надо написать функцию, которая получает из списка
# уникальные значиния, но без использования сета
#
# создает уникальный хеш а потом ставит число под этот хеш

import random

l1 = list(range(0, 1000))
l2 = l1 * 1000
random.shuffle(l2)
start = random.randint(0, len(l2))
end = random.randint(0, len(l2))
lst = l2[min(start, end): max(start, end)]
# print(lst)

a = []

for value in lst:
    if value != a[0: len(a) - 1]:
        a.append(value)


