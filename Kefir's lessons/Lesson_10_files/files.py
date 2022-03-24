

# 2 типа файлов - байт файл и текстовый код
# виз - создает контекст для того чтобы происходит внутри


# f = open('/Users/dmitryvalikov/Documents/5. Python/study/Kefir\'s lessons/Lesson_10_files/files.py', 'r')
f = open('/Users/dmitryvalikov/Documents/5. Python/study/Kefir\'s lessons/Lesson_10_files/files.py', 'rb')

# f.close() # закрыть файл

# f.flush() # смой все, что записал    ----

# f.read() # считать файл полность
# print(f.read())
# print(f.read())

# f.readline(5) # читает новую строке в файле
# print(f.readline(5))
# print(f.readline())

# f.fileno() # дескриптор - хуйня не понадобится
# print(f.fileno())

# прочитала построчно и вышла когда закончились
# while True:
#     line = f.readline()
#     if line:
#         print(line)
#     else:
#         break

# print(f.readlines())
# print(f.read().decode('cp1251'))

# print('sting'.encode())
# b'array' - строка из битов

# это и есть контекст. делаем внутри что-то, а как только вышли - закрыли  за собой
# with open('/Users/dmitryvalikov/Documents/5. Python/study/Kefir\'s lessons/Lesson_10_files/files.py', 'r') as f:
#     print(f.read())

# 'w' перезапись
with open('test', 'w') as f:
    f.write('Первая строчка новго файла')

# 'a' запись к имеющемуся
with open('test', 'a') as f:
    f.write('\nВторая строчка новго файла')

# json - как txt, но когда читаешь, он трансформирует в словарь

import json

# dump - записать в джисон - но не тюпл и сет
# сначала все сформируй а потом один раз дамп
with open('test.json', 'w') as f:
    # json.dump({'хуй': 'пизда', 'dick': 'cunt'}, f, ensure_ascii=False, indent=4)
    json.dump({'хуй': 'пизда', 'dick': {1: 1, 2:2}}, f, ensure_ascii=False, indent=4)


with open('test.json', 'r') as f:
    # data = f.read()
    data = json.load(f)
    hui = data['хуй']


print(data)
print(hui)

d = json.dumps({'хуй': 'пизда', 'dick': {1: 1, 2:2}}, ensure_ascii=False)
print(d)

d1 = json.loads(d)
print(d1)





