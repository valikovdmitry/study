


def square(x):
    res = x ** 2
    return res

def sub(x):
    res = x - 3
    return res

def mul(x):
    res = x * 6
    return res

def apply_square(*lst):
    res = [square(value) for value in lst]
    return res

def apply(*lst, function = square):
    res = [function(value) for value in lst]
    return res

# print(apply_square(1,2,3))

print(apply(1,2,3))
print(apply(1,2,3, function=mul))

sub = lambda x, y: y(x - 2)

r = sub(3, mul)
print(r)


def apply2(*lst, function = lambda x: (x + 10) if (x > 6) else (x - 5)):
    res = [function(value) for value in lst]
    return res


print(apply2(5))
print(apply2(7))


