# Filename: func_nonlocal.py

x = 1

def func_outer():
    x = 2
    print('\nNonLocal \'x\' =', x, '\n')

    def func_inner():
#        nonlocal x
#        global x
        x = 5
        print('Local \'x\' =', x)

    func_inner()

    print('\nNonLocal become =', x, '\n')

func_outer()
print('Glabal \'x\' =', x)
