def isPalindrome(x=1):
    a = input('Type a number: ')
#    print('\t Длинна числа: ', len(a))

    k = (int(len(a) / 2))
#    print('\t Половина длинны: ', k)

    e = str((a[0:k]))
    r = str((a[-k:]))
    n = list(r)
    n.reverse()
    n2 = "".join(n)

#    print('\t Первая половина числа', e)
#    print('\t Развернутая вторая половина числа', n2)


    if e == n2:
        a = input('Type a number: ')
#        print('\n', True)
        print('Число', a, '- палиндромом.')
    else:
#        print('\n', False)
        print('Число', a, 'не палиндром.')

isPalindrome()
