# 2. На входе список из любых типов переменных. Задача удалиить из списка все с типом str.

lst = [1, 0.5, 'sring', 2, 0.7, 'word', 7, 3.5, 'sea']
lst2 = [2, 1.5, 'star', 3, 8.7, 'work', 9, 4.5, 'tea']

def remove(x, y=str):
    lst_wo_str = []
    for value in x:
        if not isinstance(value, y):
            lst_wo_str.append(value)
    return lst_wo_str

def remove2(x, y=str):
    return [value for value in x if not isinstance(value, y)]


print(remove(lst))
print(lst)
lst3 = remove2(lst)
print(lst3)
