



a = [["B","C"],["D","B"],["C","A"]]
b = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
c = [["A","Z"]]


def destCity(paths) -> str:
    print(paths)
    d = dict()                         # создали словарь, где город вылета ключ, а город прилета значение
    for a, v in paths:
        d[a] = v

    lst = []                           # создали множество городов, из которых можно вылетать
    for k in d:
        lst.append(k)
    lst_set = set(lst)
    print(lst)

    for v in d.values():               # смотрим, можно ли куда то улететь из городов прилета
        if str(v) in lst_set:
            pass
        else:
            print(f'che {v} нету')

destCity(a)
destCity(b)
destCity(c)

