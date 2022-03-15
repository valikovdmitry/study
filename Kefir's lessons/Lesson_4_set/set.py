



a = {}

c = [1, 1, 2, 2, 3, 4, 4]
b = set(c)
l = [value for value in range(4, 20)]
b2 = set(l)

#print(c)
#print(b)

#print(hash('35'))
#print(3 in b)


# add
#b.add(5)
#print(b)

# remove
#b.remove(5)
#print(b)

# pop
#print(b.pop())

# copy
# d = b.copy()
#b.remove(3)
#print(b)
#print(d)

# clear
#b.clear()
#print(b)


# union  //  или
# print(b)
# print(b2)
# print(b.union(b2))
# print(b)
# b3 = b2 | b
# print(b3)
# b.update(b2)
# print(b)

# и   //   intersection
# print(b.intersection(b2))
# b4 = b2 & b
# print(b4)
# b.intersection_update(b2)
# print(b)
# print(b2)

# difference    вычитание   ,но b не меняется  //
# b4 = b.difference(b2)
# b5 = b2.difference(b)
# print(b4)
# print(b5)
# b6 = b - b2
# print(b6)
# b.difference_update(b2)
# print(b)

# xor    //   только там или только там
# y = b.symmetric_difference(b2)
# print(y)
# # b.symmetric_difference_update(b2)
# # print(b)
# z = b ^ b2
# print(z)

# issubset  /  яляется ли первое подмножеством второго
# print(b.issubset(b2))
# b3 = {1 , 2}
# print(b3.issubset(b))
#
# # issuperset  /  является ли первое надмножеством второго
# print(b.issuperset(b3))
#
# # isdisjoint  /  являются ли 2 множества НЕ пересекающимися
# print(b.isdisjoint(b3))
# print(not b.isdisjoint(b3))
#
# m1 = {1, 2}
# m2 = {3, 4}
# print(m1.isdisjoint(m2))

# discard  /  удали есть ли есть такое
# b.discard(66)
# print(b)












