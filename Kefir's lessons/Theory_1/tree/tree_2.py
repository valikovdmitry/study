lst = [1,2,3,4,5,6,7,8,9]

d = dict()
for value in lst:
    d[value] = []
    for check in lst:
        sum = value + check
        if sum % 3 != 0 and sum % 5 != 0 and sum % 7 != 0 and value != check:
            d[value].append(check)
print(d)



def create_array(x):
    count = 1
    result = [1]
    while count < 9:
        for value in x:
            prev = result[-1]
            if value in d[prev]:
                result.append(value)
                count += 1
                if count == 9:
                    break
    return result


res = create_array(lst)
print(res)


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
checkout(res)




