lst_2 = [1, 7, 10, 3, 4, 2, 5, 9, 6, 8]

def sort(x):
    l = list(x)
    l2 = []
    while len(l) > 0:
        m = max(l)
        l2.append(m)
        l.remove(m)
        continue
    return l2

print(lst_2)
print(sort(lst_2))


def sort2(x):
    l = list(x)
    l2 = []
    while len(l) > 0:
        m = min(l)
        l2.append(m)
        l.remove(m)
        continue
    return l2

print(lst_2)
print(sort2(lst_2))



