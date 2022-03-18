def f(x):
    return x
print(f)


def e(x):
    yield x
print(e)

lst = [1, 2, 3, 4, 6, 7]

sort = sorted(lst)
print(sort)

rev = reversed(lst)
print(rev)
print(list(rev))
print([v for v in rev])


# lst2 = lst.reverse()
# print(lst2)


e = enumerate(lst)
print(e)



lst2 = [2,4,6,8,10]
lst3 = [9,8,7,5]

# zip - создает пары из двух елементов списков с одинаковыми индексами от 0 до макс. И количесво пар = длине короткого списка

# print(list(zip(lst, lst2, lst3)))
# print(dict(zip(lst, lst2)))


# map - примени к каждому элементу какую то функцию

# lst4 = list(map(str, zip(lst2, lst3)))
# print(lst4)

# lst4 = list(map(lambda x: x[0] + x[1], zip(lst2, lst3)))
# print(lst4)


lst4 = dict(map(lambda x: (x[0] + 1, x[1] - 2), zip(lst2, lst3)))
print(lst4)



# filter - оставить только значение удовлетворяющие условию

lst5 = list(filter(lambda x: x < 8, lst2))
print(lst5)

################### - решить задачу со словами через фильтр


l = '/'.join(['1', '2', '3'])
print(l)


# sum - получает сумму от всех значений, от старта

print(sum(lst2, start=2))
