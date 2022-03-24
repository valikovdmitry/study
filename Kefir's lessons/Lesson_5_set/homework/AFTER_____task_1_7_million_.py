import random
l1 = list(range(0, 1000))
l2 = l1 * 1000
random.shuffle(l2)
start = random.randint(0, len(l2))
end = random.randint(0, len(l2))
lst = l2[min(start, end): max(start, end)]

l = sorted(lst)
l3 = []
for index, value in enumerate(l):
    if index == 0 or value > l3[-1]:
        l3.append(value)













print('   Уникальные значения: ', l3)
print(' Количество на страрте: ', len(l2))
print('Количество после среза: ', len(lst))
print('     Из них уникальны : ', len(l3))
print('                    От: ', start)
print('                    До: ', end, '\n')


