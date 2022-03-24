words = ["gin", "zen", "gig", "msg"]

words2 = ["noilq","kzlq","ydreq","ybxk","kzlq"]


def uniqueMorseRepresentations(words) -> int:
    morze = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.",
             "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    crypt = dict(tuple(zip(alphabet, morze)))


    de_crypt = dict()
    for word in words:
        for letter in word:
            de_crypt[word] = de_crypt.get(word, '') + crypt[letter]


    return len(set(de_crypt.values()))


print(uniqueMorseRepresentations(words))
print(uniqueMorseRepresentations(words2))


