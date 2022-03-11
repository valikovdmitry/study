

n = 23 #number
g = int() #guess
x = n == g
running = True

while running:
    g = int(input("Введите целое чиcло: "))  # guess

    if g == n:
        print('Ура! Вы угадали, это число ', n, '!', sep='')
        running = False
    elif g < n:
        print('Нужное число больше.')
    elif g > n:
        print('Нужное число меньше.')

else:
    print('Завершение.')

