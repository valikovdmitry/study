a = [["B","C"],["D","B"],["C","A"]]
b = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
c = [["A","Z"]]


def destCity(paths) -> str:
    d = dict()
    for a, v in paths:
        d[a] = None

    for a, v in paths:
        if v not in d:
            d[a] = v

    for v in d.values():
        if v != None:
            return v


print(destCity(a))
print(destCity(b))
print(destCity(c))
