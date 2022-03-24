lst = [1,2,3,4,5,6,7,8,9]
d_immut = {1: [3, 7], 2: [6, 9], 3: [1, 5, 8], 4: [7, 9], 5: [3, 6, 8], 6: [2, 5, 7], 7: [1, 4, 6, 9], 8: [3, 5, 9], 9: [2, 4, 7, 8]}
d = {1: [3, 7], 2: [6, 9], 3: [1, 5, 8], 4: [7, 9], 5: [3, 6, 8], 6: [2, 5, 7], 7: [1, 4, 6, 9], 8: [3, 5, 9], 9: [2, 4, 7, 8]}

result = [1]
stopper = 0
actual_number = 1
while stopper != 9:
    print('зашла',actual_number)
    print(stopper)
    if stopper == 8:
        result.append(d[5][0])
        break
    if d[actual_number] == []:
        print('это тупиииик')
        break
    num = d[actual_number][0]
    result.append(num)
    for value in d.values():
        if actual_number in value:
            value.remove(actual_number)
    print(f'удалили {actual_number}', d)
    print(result, '\n')
    stopper += 1
    actual_number = num
    if d[actual_number] == [3] and stopper != 9 and 7 in result or d[actual_number] == [7] and stopper != 9 and 3 in result:
        print('yes')
        result.remove(actual_number)
        print(result)
        error = actual_number
        actual_number = result[-1]
        d[actual_number].remove(error)
        print(actual_number)
        print(d)

print(result)


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

checkout(result)