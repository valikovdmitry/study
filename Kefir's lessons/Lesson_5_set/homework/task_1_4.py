
# l = list(range(1, 6))
# lst = l * 2
lst = [1, 2, 5, 3, 1, 4, 5, 3, 4, 2]
print(lst)


l = sorted(lst)
print(l)
l2 = [0]
for index in range(0, len(l)):
    if l[index] > max(l2):
        l2.append(l[index])
l2.remove(0)


print(l2)

