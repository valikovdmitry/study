lst1 = [1, 2, 4, 5, 6, 7]; k1 = 2
lst2 = [3, 2, 1, 5, 4]; k2 = 2
lst3 = [1, 2, 2, 1]; k3 = 1


def count_k_pairs(nums, k):
    sort = sorted(nums)                           # соритируем
    hash_ = dict()
    count = 0

    for exict in range(sort[0], sort[-1] + 1):    # создаем хеш таблицу с нулями
        hash_[exict] = 0

    for key in sort:                              # считаем сколько раз поподается каждая цифра
        if key in hash_:                          # получаем в значение количество определенного символа
            hash_[key] += 1

    for key, value in hash_.items():              # смотрим какое количество в листе 'n' и 'n - k'
        ans = key - k                             # если или 'n' или 'n - k' равны нулю - в 'count' ничего не пойдет,
        if ans in hash_:                          # что верно, такой пары действительно нет
            count += value * hash_[ans]           # в обратном, получаем сколько 'n' и сколько 'n - k' на входе
                                                  # считаем количество уникальных сочетаний 'n' и 'n - k'
    return count                                  # по комбинаторике это - (количество 'n') * (количество 'n - k')








print(lst1)
print(count_k_pairs(lst1, k1))
print(lst2)
print(count_k_pairs(lst2, k2))
print(lst3)
print(count_k_pairs(lst3, k3))
