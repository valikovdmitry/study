


x = 50

def f(x):
    print('x =', x)
    x = 2
    print('local x =', x)
    s = 10 * x
    print('10 * local x = ', s)

f(x)
print('\nnative x still =', x)