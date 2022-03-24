



d = {
    'Name': 'Dmitry',
    'Last name': 'Valikov'
}

d1 = dict()

# print(d['Name'])
# # print(d['Name2'])
#
# # выдает либо ноне либо то, что мы хотим если нет такого ключа
# print(d.get('Name2', 'Hui  vam'))
#
# # проверка есть ли такой ключ
# print('Name2' in  d)
#
# # добавление ключа со значение или замена значения по ключу
# d['Name3'] = 'Jordan'
# print(d)
d['Name3'] = 'Lebron'
# print(d)
#
# # len считает количество ключей
# print(len(d))

# итерации

# # по ключам
# for key in d.keys():
#     print(key)
# for key in d:
#     print(key)
#
# # по значениям
# for value in d.values():
#     print(value)

# # по парам
# for key, value in d.items():
#     print(f'{key} --- {value}')

# # pop - удаление по ключу
# print(d.pop('Name3'))
# print(d)

# # clear
# d.clear()
# print(d)

# # popitem - удаление последнего ключа, возвращает 'ключ : значени'
# print(d.popitem())
# print(d)

# # объединяет словари   //   добавляет ключи, которых не было   ///   и меняет значения в ключах, которые совпали
# d2 = {'Name': "Nikolay", 'Car': 'Bmw'}
# d.update(d2)
# print(d)
#
# # добавлет ключ/значение если его нет в словаре / а если есть, то он нихуя не делает
# d.setdefault('Name', 'Airbus')
# print(d)



l = {
    'first': [],
    'second': {},
    'third': dict()
}

names = ['Вася Пупкин', 'Петя Петров', 'Иван Пупкин', 'Саша Петров', 'Володя Пупкин']

l2 = {}

for full_name in names:
    name, last_name = full_name.split()
    if last_name not in l2:
        l2[last_name] = []
    l2[last_name].append(name)
print(l2)














