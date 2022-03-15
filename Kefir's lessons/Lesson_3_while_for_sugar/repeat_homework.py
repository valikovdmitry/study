a = [value for value in range(1, 11)]
b = [value for value in range(10, 21)]

def reverse_while(x):
    value = len(x) - 1
    l = []
    while value >= 0:
        l.append(x[value])
        value -= 1
    print(l)
reverse_while(a)
reverse_while(b)

def reverse_for(x):
    l = []
    for index in range(len(x) - 1, -1, -1):
        l.append(x[index])
    print(l)
reverse_for(a)
reverse_for(b)

def reverse_sahar(x):
    l = [x[index] for index in range(len(x) - 1, -1, -1)]
    print(l)
reverse_sahar(a)
reverse_sahar(b)

