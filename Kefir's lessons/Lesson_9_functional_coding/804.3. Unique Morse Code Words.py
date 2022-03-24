# words = ["gin", "zen", "gig", "msg"]
words = ["noilq","kzlq","ydreq","ybxk","kzlq"]
# words = ["yxmine","yxzd","eljys","uiaopi","pwlk"]


morze = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--..", ',']
# alphabet = 'abcdefghijklmnopqrstuvwxyz,'

de_crypt = dict()
for word in set(words):
    decrypt_word = ''
    for index, letter in enumerate(word):
        alph = ord(letter) - 97
        de_crypt[word] = de_crypt.get(word, '') + morze[alph]
print(de_crypt)

equal = dict()
for value in de_crypt.values():
    equal[value] = 0

print(equal)
print(len(equal))





print(ord('z'))







'-.---...-..--.-'
'-.---...-..--.-'
'-.---...-..--.-'
'-.---...-..--.-' # если в ручную
'-.---...-..--.--.---...-..--.-'# kzlq
# print(str(crypt['k'] + crypt['z'] + crypt['l'] + crypt['q']))





