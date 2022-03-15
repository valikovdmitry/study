a = []
for i in range(20,31):
    a.append(i)
print(a)

result = []
for index in range(0, len(a)):
    if index != 0:
        result.append(a[-index])
result.append(a[0])
print(result)









