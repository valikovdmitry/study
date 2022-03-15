
jewels = "aAce"
stones = "aAAbbcacbbcAe"

def counter(x):
    index = 0
    a = 0
    while index < len(x):
        for value in stones:
            if value == x[index]:
                a += 1
        index += 1

    return a

print(counter(jewels))

