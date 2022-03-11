x = 50

def f2():
    x = 50
#    global x

    print('x =', x)
    x = 2
    print('replased x =', x)

f2()
print('\n \t Native \'x\' doesn\'t changed:', x)

def f():
#    x = 40
    global x

    print('\nx =', x)
    x = 40
    print('replased x =', x)


f()
print('\n \t Native \'x\' changed to:', x)
