sentence = "jwtucoucmdfwxxqnxzkaxoglszmfrcvjoiunqqausaxxaaijyqdqgvdnqcaihwilqkpivenpnekioyqujrdrovqrlxovcucjqzjsxmllfgndfprctxvxwlzjtciqxgsxfwhmuzqvlksyuztoetyjugmswfjtawwaqmwyxmvo"
s2 = "thequickbrownfoxjumpsoverthelazydog"


def checkIfPangram(self, sentence: str) -> bool:
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    sentence_set = set(sentence)
    dif = sentence_set - alphabet
    return len(dif) == 0 and len(sentence_set) == 26








print(checkIfPangram(sentence, sentence))
print(checkIfPangram(s2, s2))




