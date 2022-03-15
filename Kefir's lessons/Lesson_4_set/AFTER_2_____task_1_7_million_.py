import random
l1 = list(range(0, 1000))
l2 = l1 * 2
random.shuffle(l2)
start = random.randint(0, len(l2))
end = random.randint(0, len(l2))
lst = l2[min(start, end): max(start, end)]

l = [None] * 1000

for value in lst:
    l[value] = value

l = [value for value in l if value is not None]

print(l)












