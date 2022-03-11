


n = 5
x = n > 1

print(n)
while n > 1:
    n = n - 1
    print(n)
else:
    while True:
        n = n + 1
        print(n)
        if n == 15:
            break

l = []
for i in range(0, 11, 2):
    l.append(i)
    if i == 4:
        break
print(l)


