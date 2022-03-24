
l = list(range(1, 6))
lst = l * 2
print(l)

a = [1, 2, 3, 4]
print(a)

for index in range(0, len(a) - 1):
    for value in l:
        if value == a[index]:
            a.append(value)

print(a)




