e = {5: None, 3: 'ccccc', 1: 'aaaaa', 2: 'bbbbb', 5: 'eeeee', 4: 'ddddd'}
m = max(e) + 1
f = {}
b = dict()
print(e)
lohi = []
lohi_detected = []

expected_key = 1
while expected_key < m:
    print(expected_key)
    for key, value in e.items():
        if key not in f:
            f[key] = []              # создали в финальном словаре ключи равные ключам исходной библиотеки
    for key, value in e.items():
        prev = key - 1
        print(key, value)
        if key == expected_key:      # если исходный ключ совпал с тем, что мы ждем - добавяем в финальный словарь
            f[key] = value
            lohi_detected = list(lohi)
        if key > expected_key:       # если он больше ожидаемого ключа, мы добавляем его значение в буфер словарь
            # if key not in b:
            #     b[key] = []
            b[prev] = value
            lohi.append(key)

        print('Buffer:', b)
        print(' Final:', f)
        print('  Lohi:', lohi)
        print(lohi_detected)
    lohi2 = list(lohi_detected)
    print(lohi2)
    expected_key += 1                 # после меняем ожидаемый ключ

print(f)

