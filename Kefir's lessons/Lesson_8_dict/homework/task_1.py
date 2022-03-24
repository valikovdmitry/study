
jewels = "aAce"
stones = "aAAbbcacbbcAe"

def counter(x):
    index = 0
    a = []
    while index < len(x):
        for value in stones:
            if value == x[index]:
                a.append(value)
        index += 1

    print(a)
    print(len(a))

counter(jewels)
