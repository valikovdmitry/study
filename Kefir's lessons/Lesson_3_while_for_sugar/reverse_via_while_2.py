a = []
for i in range(1,11):
    a.append(i)
print(a)

index = len(a) - 1
b = []
while index >= 0:
    b.append(a[index])
    index -= 1
print(b)

result = []
for index in range(len(a) -1, -1, -1):
    result.append(a[index])
print(result)

result2 = [a[index] for index in range(len(a) - 1, -1, -1)]
print(result2)








