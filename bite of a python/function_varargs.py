

def total(a=5, *numbers, **phonebooks):
    print('a =', a)

    # проход по всем элементам кортежа
    for single in numbers:
        print('single =', single)

    # проход по всем элементам словаря
    for first_part, second_part in phonebooks.items():
        print(first_part, second_part)

total(10, 1, 2, 3, 4, 5, Jack=1123, John=2231, Inge=1560)