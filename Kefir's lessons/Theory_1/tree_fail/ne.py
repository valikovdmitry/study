a = [1, 3, 7, 4, 9, 2, 6, 5, 8]
b = [1, 3, 7, 4, 9, 8, 5, 6, 2]
c = [1, 7, 4, 9, 2, 6, 5, 3, 8]
d = [1, 7, 4, 9, 2, 6, 5, 8, 3] # верная
e = [1, 7, 4, 9, 8, 3, 5, 6, 2]



def checkout(x):
    s = dict()
    for index, value in enumerate(x):
        s[value] = ''
        prev = x[index - 1]
        sum = value + prev
        if sum % 3 != 0 and sum % 5 != 0 and sum % 7 != 0:
            s[value] = f'OK'
        else:
            s[value] = f'ERROR'
    print(s)

checkout(a)
checkout(b)
checkout(c)
checkout(d)
checkout(e)
