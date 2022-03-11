c = 'Sample '
b = '\n \t text'
d = '''
Текст
который
будет
на нескольих
строках
который'''
e = '''Простой {1} текст, которыя я придумал {1} {0}'''
f = f'Простой {b}'



#print('который' in d)
#print(d.find('который'))
#print(d.replace('который', 'каторый'))

# приведение типов

# int
r = int(5)
#print(float(r))
#print(str(r))
#print(bool(r))

# float
u = float(5.6)
#print(u)
#print(int(u))
#print(str(u))
#print(bool(u))

# string
new_string = '5.6'
#print(new_string)
#print(int(new_string))
#print(float(new_string))
#print(bool(new_string))
#print(int(float(new_string)))


# провека типа переменной
#print(type(u))
#print(type(new_string))
#print(type(r))

print(isinstance(u, float))

help(isinstance)
