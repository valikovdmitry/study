# 2. На входе список из любых типов переменных. Задача удалиить из списка все с типом str


lst = [1, 0.5, 'sring', 2, 0.7, 'word', 7, 3.5, 'sea']

print(lst)

for value in lst:
    if (isinstance(value, str)) == True:
        print(value)