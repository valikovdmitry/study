import random

l1 = list(range(0, 10))
l2 = l1 * 3
random.shuffle(l2)
print(l2)

l = sorted(l2)
print(l)

l3 = [0]
for index in range(0, len(l)):
    if l[index] > max(l3):
        l3.append(l[index])
l3.remove(0)

print(l3)


