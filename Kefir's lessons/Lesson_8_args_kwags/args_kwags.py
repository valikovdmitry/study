def func(x, *args, **kwargs):
    print(args)
    print(kwargs)


# func('love', 1, 2, False, 'a', **{'1': 1, '2':2, '3':3})

func('love', 1, 2, False, 'a', b=1, c=2, d=3)


def max_(*args):
    return max(args)


print(max_(1, 2, 3, 4, 5, 6, 7))

# help(print)


# print(1,2,3,4,5,6,7, sep='/')
#
#
# def func1(x, y, z, *args, d=5, **kwargs):
#     a = args * d
#     return a
#
# print(func1(5, 6, 3, 5, 6, c=[]))

c = []


def append_(c):
    c = []
    c.append(1)
    print(c)


append_()
append_()
append_()
append_()



