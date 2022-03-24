
def sum(x):
    if x < 2:
        return True
    else:
        return False

    return

print(sum(1))


def sum2(x):
    if x < 2:
        return True
    elif x >= 3:
        return False

    return


print(sum2(1))

l = []

def our_enumerate(lst):
    result = []
    index = 0
    for value in lst:
        result.append((index, value))
        index += 1
    return result


print(our_enumerate(range(1, 10)))


def our_enumerate2(lst):
    index = 0
    for value in lst:
        yield index, value
        index += 1



print(our_enumerate2(range(1, 10)))

l2 = our_enumerate2(range(1, 10))

for index, value in l2:
    print(index, value)


def func3():
    yield 3
    yield 4
    yield 5
    yield 6

for v in func3():
    print(v)