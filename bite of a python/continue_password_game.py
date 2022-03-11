
l = []

while True:
    s = input('Type code word in 3 symbols: ')
    if s == 'save':
        break
    if len(s) < 3:
        print('Too small code word.')
        continue
    if len(s) > 3:
        print('Too large code word.')
        continue
    print('Great! Your code is \'', s, '\'. Type \'save\' to save the code. Type another code here to change it.', sep='')
    l.append(s)
print('Done!')
print('Your code word is ', l)
print(l[0])

while True:
    i = input('Enter your password: ')
    if i == l[0]:
        break
    if i != l[0]:
        print('Password is incorrect. Try another.')
print("Correct. You\'re in.")