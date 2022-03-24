import random

a = [value for value in range(1, 11)]
b = [value for value in range(10, 21)]


def delete(x):
    l = []
    for value in x:
        if value % 2 == 0:
            l.append(value)
    print(l)
delete(b)


def delete2(x):
    l = [value for value in x if value % 2 == 0]
    return l

print(delete2(b))
lst = delete2(b)
print(lst)

lst_2 = [1, 7, 10, 3, 4, 2, 5, 9, 6, 8]
random.shuffle(a)
print(a)

def sort(x):
    l = list(x)
    l2 = []
    while len(l) > 0:
        l2.append(max(l))
        l.remove(max(l))
        continue
    return l2

print(sort(lst_2))
print(lst_2)


def sort2(x):
    l = list(x)
    l2 = []
    while len(l) > 0:
        l2.append(min(l))
        l.remove(min(l))
        continue
    return l2

print(sort2(lst_2))
print(lst_2)


print(a)

