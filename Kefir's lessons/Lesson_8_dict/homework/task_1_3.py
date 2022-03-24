
jewels = "aAce"
jewels2 = "aAe"
stones = "aAAbbccacbbcAe"


def counter(jewels):
    uniq = set(jewels)
    count = 0
    for stone in stones:
        if stone in uniq:
            count += 1
    return count

print(counter(jewels))
print(counter(jewels2))



