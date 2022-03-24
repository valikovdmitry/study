# words = ["gin", "zen", "gig", "msg"]
words = ["noilq","kzlq","ydreq","ybxk","kzlq"]
# words = ["yxmine","yxzd","eljys","uiaopi","pwlk"]


morze = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--..", '/']
alphabet = 'abcdefghijklmnopqrstuvwxyz/'
crypt = dict(tuple(zip(alphabet, morze)))

de_crypt = dict()
for word in set(words):   # вся проблема была в том, что эта сука подкинула в одном списке 2 одинаковых слова
    for letter in word:
        de_crypt[word] = de_crypt.get(word, '') + crypt[letter]
print(de_crypt)

equal = dict()
for value in de_crypt.values():
    equal[value] = 0

print(equal)
print(len(equal))

crypt = dict(tuple(zip(alphabet, morze)))
print(crypt)








'-.---...-..--.-'
'-.---...-..--.-'
'-.---...-..--.-'
'-.---...-..--.-' # если в ручную
'-.---...-..--.--.---...-..--.-'# kzlq
# print(str(crypt['k'] + crypt['z'] + crypt['l'] + crypt['q']))





