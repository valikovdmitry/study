d = 6
f = False


if d < 6:
    c = 1
else:
    c = 2


c = 1 if d < 6 else 2

print(c)


def func(x):
    return x ** 2

# c = 4


e = func(d) if (d != 0) and (not f) or (c is not None) else 0

# print(e)


# когда выражение 'if c' будет равно 'false'

c = None

c = 0
if not c:
    print('Да')

c = ''
if not c:
    print('Да')

c = []
if not c:
    print('Да')

c = {}
if not c:
    print('Да')