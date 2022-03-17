input = [1,2,3,1,1,3]
input1 = [1,1,1,1]
input2 = [1,2,3]


def good_pairs(x):
    formula = int((x * (x - 1)) / 2)
    return formula

def count(x):
    amount = 0
    for value in range(min(x), max(x) + 1):
        if x.count(value) > 1:
            amount += good_pairs(x.count(value))
    print(x)
    print(amount)

count(input)
count(input1)
count(input2)







