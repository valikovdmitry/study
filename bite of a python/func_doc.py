


def max(x,y):
    '''Находит наибольшее число.

Оба значения должны быть целыми числами.
Оба значения должны быть целыми числами.
Оба значения должны быть целыми числами.'''

    x = int(x)
    y = int(y)

    if x > y:
        print(x, 'наибольшее число')
    else:
        print(y, 'наибольшее число')

max(1, 2)
print()
print(max.__doc__)