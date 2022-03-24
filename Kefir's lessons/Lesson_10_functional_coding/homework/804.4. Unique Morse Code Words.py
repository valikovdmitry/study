# words = ["gin", "zen", "gig", "msg"]
# words = ["noilq","kzlq","ydreq","ybxk","kzlq"]
words = ["yxmine","yxzd","eljys","uiaopi","pwlk"]


morze = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..', '/': '/'}
words_str = '/'.join(words)
print(words_str)

crypted = str()
for letter in words_str:
    crypted += morze[letter]

result = set(crypted.split('/'))
print(result)

print(len(result))



















