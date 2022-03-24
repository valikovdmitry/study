



d = {'1': '5', '2': '10', '3': '15', '4': '20'}

c = dict()
c['1'] = '5'


# print(d)
# print(c)
#
# print(c['1'])
# print(c.get(2, 'Do not exist.'))
# print('1' in d)
# print('2' in d)
#
# d['1'] = '2'
# print(d)
# print(len(d))

# for key in d:
#     print(key)
# for value in d.values():
#     print(value)
# for key, value in d.items():
#     print(key, value)

# print(d.pop('3'))
# print(d)



lst = list(range(0,20))
s = {'Меньше 15': [], 'Больше 15': []}



for full in lst:
    if full < 15:
        s['Меньше 15'].append(full)
    elif full > 15:
        s['Больше 15'].append(full)
print(s)


nums = [8,2,1,2,3]
result = {'n1': [], 'n2': [], 'n3': [], 'n4': [], 'n5': []}

for value in nums:
    if value < nums[0]:
        result['n1'].append(value)
    elif value < nums[1]:
        result['n2'].append(value)

print(result)








