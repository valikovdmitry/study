

def func(x):
    for i in range(0, 51, x):
        print(i)
    else:
        i = 50
        print('_____', i, '_____')
        while i > 5:
            i = i - x
            print(i)

func(10)