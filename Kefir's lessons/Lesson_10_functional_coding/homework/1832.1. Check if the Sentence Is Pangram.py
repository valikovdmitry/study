sentence = "jwtucoucmdfwxxqnxzkaxoglszmfrcvjoiunqqausaxxaaijyqdqgvdnqcaihwilqkpivenpnekioyqujrdrovqrlxovcucjqzjsxmllfgndfprctxvxwlzjtciqxgsxfwhmuzqvlksyuztoetyjugmswfjtawwaqmwyxmvo"
s2 = "thequickbrownfoxjumpsoverthelazydog"


def checkIfPangram(self, sentence: str) -> bool:
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    s_alphabet = set(alphabet)
    count = 0


    for letter in s_alphabet:
        if letter in set(sentence):
            count += 1


    return count == 26


print(checkIfPangram(sentence, sentence))
print(checkIfPangram(s2, s2))



