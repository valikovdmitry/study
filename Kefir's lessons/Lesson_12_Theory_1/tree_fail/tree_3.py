lst = [1,2,3,4,5,6,7,8,9]
d = {1: [3, 7], 2: [6, 9], 3: [1, 5, 8], 4: [7, 9], 5: [3, 6, 8], 6: [2, 5, 7], 7: [1, 4, 6, 9], 8: [3, 5, 9], 9: [2, 4, 7, 8]}

def checkout(x):
    s = dict()
    for index, value in enumerate(x):
        s[value] = ''
        prev = x[index - 1]
        sum = value + prev
        if sum % 3 != 0 and sum % 5 != 0 and sum % 7 != 0:
            s[value] = f'{prev} + {value} = {sum} OK/'
        else:
            s[value] = f'{prev} + {value} = {sum} ///ERROR///.'
    print(s)

def create_array(x):
    count = 1
    result = []
    while count < 9:
        for value in x:
            if result == []:
                result.append(value)
            prev = result[-1]
            if value in d[prev]:
                print('value: ', value)
                print('prev: ', prev)
                print('allowed: ', d[prev])
                print('- ', value in d[prev])
                result.append(value)

                d[value].remove(prev)

                prev = value
                count += 1
                print(f'Добавили {value} в список lst -----------------')
                print('count', count)
                print('result', result)

                print(d[value])
                print(prev)


                print('\n\n')
                if count == 9:
                    break
    return result

# res = create_array(lst)
# print(res)
# checkout(res)

d[1].pop(0)

# res2 = create_array(lst)
# print(res2)
# checkout(res2)

d[7].pop(3)
print(d)

res3 = create_array(lst)
print(res3)
checkout(res3)


