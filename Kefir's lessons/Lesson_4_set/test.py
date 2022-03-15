import random

s = random.randint(0,200000)
s2 = str(s)
s3 = s2[::5]
print(s2)

def fun(x):
    a = str(x)
    b = 'a[:-3], '.', a[-3:], sep='''

fun(s)