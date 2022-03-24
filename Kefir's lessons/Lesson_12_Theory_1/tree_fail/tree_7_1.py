lst = [1,2,3,4,5,6,7,8,9]
d = {1: [3, 7], 2: [6, 9], 3: [1, 5, 8], 4: [7, 9], 5: [3, 6, 8], 6: [2, 5, 7], 7: [1, 4, 6, 9], 8: [3, 5, 9], 9: [2, 4, 7, 8]}

results = dict()

for key, value in d.items():
    results[1] = key, value

print(results)