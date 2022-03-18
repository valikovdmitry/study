nums = [8,1,2,2,3]
nums2 = [6,5,4,8]
nums3 = [7,7,7,7]
print(nums)

def func(x):
    result = dict()
    for value in x:
        result[value] = 0
    for value in x:
        for key in result:
            if value < key:
                result[key] += 1
    return [result[value] for value in x]
# print(func(nums))


def func2(input):
    input_sorted = sorted(input) # сортируем входящие данные
    count = 0 # инициализируем счетчик
    result = dict() # инициализируем словарь со счетчиком для каждого входящего числа
    prev = input_sorted[0] # предыдущий элемент
    print(input_sorted)

    for index, value in enumerate(input_sorted): # получаем из сортированного списка индекс и значение
        print('value', value)
        print('prev', prev)
        if prev != value: # сравниваем, чтобы понять пришло ли новое значение
            result[prev] = count # если пришло, значит старое число создает ключ имени себя в результате
            count = index # обновляем каунт
            prev = value # prev = inpur_sorted[1]
        print(result)
        print('-- count', count)
    result[prev] = count

    print([result.get(value, 0) for value in input])


func2(nums)

