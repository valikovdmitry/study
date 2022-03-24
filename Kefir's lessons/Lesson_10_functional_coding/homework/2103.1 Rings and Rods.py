




rings = "B0B6G0R6R0R6G9"

def countPoints(self, rings: str) -> int:
    d = dict()
    pairs = tuple(zip(rings[1::2], rings[0::2]))       # по сути разбиваем исходный список по парам


    for rod_, ring_ in pairs:                          # смотрим сколько и каких колец попало на палку
        d[rod_] = d.get(rod_, [])
        if ring_ not in d[rod_]:
            d[rod_].append(ring_)


    count = 0                                          # если ключ содержит все цвета - добавляем в счетчик
    for v in d.values():
        if len(v) == 3:
            count += 1


    return count

print(countPoints(rings, rings))


