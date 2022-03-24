a = []
for i in range(1,11):
    a.append(i)
print(a)

index = 1
b = []
while index < len(a):
    b.append(a[-index])
    index += 1
b.append(a[0])
#print(b)

result = []
for value in range(0, len(a)):
    if value != 0:
        result.append(a[-value])
result.append(a[0])
#print(result)

print(a[-10])
print(a[9])

result2 = []
for index2 in range(1, len(a) + 1):

        result2.append(a[-index2])

print(result2)










