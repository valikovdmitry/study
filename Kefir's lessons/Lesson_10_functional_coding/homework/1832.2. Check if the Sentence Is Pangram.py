sentence = "jwtucoucmdfwxxqnxzkaxoglszmfrcvjoiunqqausaxxaaijyqdqgvdnqcaihwilqkpivenpnekioyqujrdrovqrlxovcucjqzjsxmllfgndfprctxvxwlzjtciqxgsxfwhmuzqvlksyuztoetyjugmswfjtawwaqmwyxmvo"
s2 = "thequickbrownfoxjumpsoverthelazydog"


def checkIfPangram(self, sentence: str) -> bool:
    set_sentence = set(sentence)
    return len(set_sentence) == 26






print(checkIfPangram(sentence, sentence))
print(checkIfPangram(s2, s2))



