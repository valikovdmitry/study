

allowed = "cad"
words = ["cc","acd","b","ba","bac","bad","ac","d"]
result = []
error = 0


for word in words:
    for letter in word:   # это точно остается
        if letter not in allowed:
            error += 1
    if error == 0:
        result.append(word)
    error = 0
print(len(result))

#  упростить, словари не нужны
