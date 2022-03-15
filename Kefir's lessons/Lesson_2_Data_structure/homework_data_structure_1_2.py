# 1. выведи все функции из массива значение которых по модулю 5 < 2

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

def find(s, y=5):
    result = []
    for value in s:
        x = value % y
        if x < 2:
            result.append(value)
    return result

print(find(lst))











