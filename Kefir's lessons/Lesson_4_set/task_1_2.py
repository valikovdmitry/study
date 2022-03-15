# допустин
#
# надо написать функцию, которая получает из списка
# уникальные значиния, но без использования сета
#
# создает уникальный хеш а потом ставит число под этот хеш

l = list(range(1, 6))
lst = l * 2
print(l)

a = [1, 2, 3, 4]
print(a)


for value in l:
    if value != a[0]:
        if value != a[1]:
            if value != a[2]:
                if value != a[3]:
                    a.append(value)

print('\n', a, sep='')




