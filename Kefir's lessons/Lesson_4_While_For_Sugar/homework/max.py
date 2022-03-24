l = [-1, 7, 3, -33, 4, 2, 5, 9, 6, 8]

def max2(x):
    l2 = [0]
    for index in range(0, len(l)):
        if l[index] > l2[0]:
            l2.remove(l2[0])
            l2.append(l[index])
    print(l2)

max2(l)



def max3(x):
    l2 = 0
    for index in range(0, len(l)):
        if l[index] > l2:
            l2 =l[index]
    print(l2)

max3(l)


def min1(x):
    l2 = 0
    for index in range(0, len(l)):
        if l[index] < l2:
            l2 =l[index]
    print(l2)

min1(l)



