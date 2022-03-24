# data structure

def findall(s, z=1):
    result = []
    for value in enumerate(s):
        if value[1] == z:
            result.append(value[0])
    return (result)

lst = [4, 1, 2, 7]
lst.append(1)

#print(sorted((lst))

lst2 = list()
lst2.append(1)
lst2.append(2)
lst2.append(3)
lst2.append(4)

#print(lst)
#print(lst2)


#  pop по индексу + возврат, remove по значению без возрата

#print(len(lst))
#print(lst[0], lst2[-1])
#print(lst[0:4])
#print(list(reversed(lst)))
#print(sorted(lst))

# итератор - хуйня которая двигается по списку

#print(sorted(lst, reverse=True))
#print(list(reversed(sorted(lst))))
#___________________________________

# функция

def formula(x, y, w=0):
    z = x + y
    return z

#print(formula(1, 1))
#___________________________________


#
#
# print(lst.count(5))
# print(lst.pop())
# print(lst.pop(0))
#
# print(lst)
# z = lst.pop(0) * lst.pop(0) * lst.pop(-1)
#
#
# print()
# print(lst)
# print(z)
#
#
lst3 = [3, 4, 5, 7, 1, 90]
#
# lst3.sort()
# print(lst3)
#
# lst4 = lst3
# lst4.pop(0)

print(lst3)

lst5 = lst3.copy()
lst5.pop(0)

print(lst3, lst5)
#
# lst2.extend(reversed(lst5))
# print(lst5)
#
# print(lst5.index(7))

#lst5.pop(lst5.index(7))
# print(lst5)

#print(lst5.index(99, 0, 5))
# print(5 in lst5)

# lst5.insert(0, 5)
# print(lst5)
#
# lst5[2] = lst5[4]
# print(lst5)
#
# print('\n \n \n', lst5)
# lst5.reverse()
# print(lst5)

#l = reversed(lst5)
#



#print(lst5)
#lst5.remove(90)
#lst5.remove(90)

#lst5.extend([1, 1])

#print(lst5)

#print(list(enumerate(lst5)))
#print()


#result = []

#for value in enumerate(lst5):
#    if value[1] == 1:
#        result.append(value[0])
#print(result)



#print(findall(lst3, 4))


#lst7 = lst5 * 100
#print(lst7)



#print(min(lst5))
#print(max(lst5))


