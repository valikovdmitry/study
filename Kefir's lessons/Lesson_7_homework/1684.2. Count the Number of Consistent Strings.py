

allowed = "cad"
words = ["cc","acd","b","ba","bac","bad","ac","d"]
result = []
error = 0
set_ = set(allowed)

counter = 0
for word in words:
    for letter in word:   # это точно остается
        if letter not in set_:
            error += 1
    if error == 0:
        counter += 1
    error = 0
print(counter)

