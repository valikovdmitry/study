# когда берешь енумирейт тебе возвращают tuple




t = tuple()

print(t)
print(type(t))

t1 = (1, 2, 3.5, 'str')

print(t1)

l1 = list(t1)
print(l1)

t2 = tuple(l1)
print(t2)

d = {'1': 1, '2': 2, '3':3}
t3 = tuple(d)
print(t3)


def func(x):
    return x ** 3, x * 3

print(func(2))

print(t3[1])

v1, v2, v3 = t3
print(v1, v2, v3)

# mutable и immutable

i = 5
i += 1

s = 'hui'
s = s + 'shit'
print(s)


# frozen set

f = frozenset(d)
print(f)
f1 = set(d)
print(f1)
print(f == f1)
f2 = f1.copy()

print(id(f1), id(f2))