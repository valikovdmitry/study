nums1 = [1,2,4,5,6,7]; k1 = 2
nums2 = [3,2,1,5,4]; k2 = 2
nums3 = [1,2,2,1]; k3 = 1
#                                                               # есть условие, что     1 <= nums.length <= 200
#                                                                                       1 <= nums[i] <= 100

def count_k_pairs(lst, minus_value):
    sort = sorted(lst)                                 # тут проход максимум на 200 (460)   //   сортируем
    d = dict()
    count = 0

    for exict in range(sort[0], sort[-1] + 1):         # тут проход максимум на 100   //   создаем хеш таблицу с нулями
        d[exict] = 0

    for value in sort:                                 # тут проход максимум на 200   //   считаем сколько повторений
        if value in d:
            d[value] += 1

    for key, value in d.items():                       # тут проход максимум на 100   //   выполняем подсчет
        ans = key - minus_value
        if ans in d:
            count += value * d[ans]

    return count                                       # в сумме 600 проходов максимум (860)








print(nums1)
print(count_k_pairs(nums1, k1))
print(nums2)
print(count_k_pairs(nums2, k2))
print(nums3)
print(count_k_pairs(nums3, k3))
