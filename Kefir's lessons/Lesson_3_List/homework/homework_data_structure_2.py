# 2. На входе список из любых типов переменных. Задача удалиить из списка все с типом str.

lst = [1, 0.5, 'sring', 2, 0.7, 'word', 7, 3.5, 'sea']
lst2 = [2, 1.5, 'star', 3, 8.7, 'work', 9, 4.5, 'tea']

def remove(x, y=str):
    print('\n', x)
    for value in x:
        if (isinstance(value, y)) == True:
            x.remove(value)
    print('\n \t After remove str:', '\n', '\t', x)

remove(lst)
remove(lst2)















