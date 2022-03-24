i = "aaaabbbbcccc"
i2 = "rat"
i3 = "leetcode"


def sortString(s):
    d = dict()
    a = ''

    for v in sorted(s):
        d[v] = d.get(v, 0) + 1

    while min(d.values()) > 0:
        for v in d:
            print(v)
            if d[v]:
                a += v
                d[v] -= 1
        for v in reversed(d):
            print(v)
            if d[v]:
                a += v
                d[v] -= 1

    print(d)
    print(a)








sortString(i)
sortString(i3)

