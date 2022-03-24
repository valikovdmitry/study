import random

l1 = list(range(0, 100))
l2 = l1 * 5
random.shuffle(l2)
start = random.randint(0, len(l2))
end = random.randint(0, len(l2))
lst = l2[0: end]

# print('Полный перемешанный список: ', l2)
print('          Вырезанный кусок: ', lst)

l = sorted(lst)
l3 = [-1]
for index in range(0, len(l)):
    if l[index] > max(l3):
        l3.append(l[index])
for value in l3:
    if value == -1:
        l3.remove(value)

print('          После сортировки: ', l)
print('       Уникальные значения: ', l3)
print('     Количество на страрте: ', len(l2))
print('    Количество после среза: ', len(lst))
print('         Из них уникальны : ', len(l3))
print('От: ', start)
print('До: ', end)

all_list = range(0, 1000)
all = set(all_list)
s = set(l3)
print('Нет: ', len(l1) - len(s), 'штук.')
# print('Это: \n', all.difference(s), sep='')


