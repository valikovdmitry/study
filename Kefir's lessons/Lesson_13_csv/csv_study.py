import csv

# cvs - это как xls, только там только данные, но без метаданных о цвете, шрифтах и тд


with open('test.csv', 'r') as f:
    r = csv.reader(f, delimiter=';')
    header = next(r)
    for line in r:
        print(line)
    print(header)



with open('test1.csv', 'w') as f:
    w = csv.writer(f, delimiter=';')
    w.writerow(['Spam'] * 5 + ['Baked Beans'])
    w.writerow(['','','','','',5])
