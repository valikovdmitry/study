



def s(x,y):
    print('Результат:', x + y)
    print('\n \n \n')

while True:
    x = int(input('Введите первое число от 1 до 9: '))
    if x > 9:
        print('Слишком большое число, попробуйте еще раз.')
        continue
    y = int(input('Введите второе число от 1 до 9: '))
    if y > 9:
        print('Слишком большое число, попробуйте еще раз.')
        continue
    s(x,y)
    break

