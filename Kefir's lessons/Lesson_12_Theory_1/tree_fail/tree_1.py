# написать закольцованную последовательность чисел, состоящую от 1 до 9 так,
# чтобы каждое каждая сумма соседних чисел НЕ была кратна 3, 5, 7

lst = [1,2,3,4,5,6,7,8,9]

d = dict() # сначала надо найти валидные пары, как мы делали в таблице
for value in lst:
    d[value] = []
    for check in lst:
        sum = value + check
        if sum % 3 != 0 and sum % 5 != 0 and sum % 7 != 0 and value != check:
            d[value].append(check)
print(d)

count = 1

while count < 9:
    for value in lst:
        prev = result[-1]
        if value in d[prev]:
            # print('value: ', value)
            # print('check: ', prev)
            # print('allowed: ', d[prev])
            # print('is it il allowed? :', value in d[prev], )
            result.append(value)
            prev = value
            count += 1
            # print(f'Добавили {value} в список lst -----------------')
            # print('count', count)
            # print('result', result)
            if count == 9:
                break


print(result)

s = dict()

for index, value in enumerate(result):
    s[value] = ''
    prev = result[index - 1]
    sum = value + prev
    if sum % 3 != 0 and sum % 5 != 0 and sum % 7 != 0:
        s[value] = f'{prev} + {value} = {sum} OK/'
    else:
        s[value] = f'{prev} + {value} = {sum} ///ERROR///.'
print(s)



# print(3 in d[1])



