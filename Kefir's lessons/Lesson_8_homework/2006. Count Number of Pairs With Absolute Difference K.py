

nums = [3,2,1,5,4]
k = 2
#                                                               # есть условие, что     1 <= nums.length <= 200
#                                                                                       1 <= nums[i] <= 100

count = 0
for value in nums:                    # тут 200 проходов максимум
    for check in nums:                # тут еще 200 проходов в каждом
        dif = value - check
        if dif == 2:
            count += 1                # 40.000 проходов максимум


print(count)