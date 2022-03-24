import random
l1 = list(range(0, 1000))
l2 = l1 * 1000
random.shuffle(l2)
start = random.randint(0, len(l2))
end = random.randint(0, len(l2))
lst = l2[min(start, end): max(start, end)]

l = sorted(lst)
l3 = [-1]
for index in range(0, len(l)):
    if l[index] > max(l3):
        l3.append(l[index])
        print('.')
for value in l3:
    if value == -1:
        l3.remove(value)











print('   Уникальные значения: ', l3)
print(' Количество на страрте: ', len(l2))
print('Количество после среза: ', len(lst))
print('     Из них уникальны : ', len(l3))
print('                    От: ', start)
print('                    До: ', end)


