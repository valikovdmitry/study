

str = 'поехали в питер кататьс по набережным'

a = ord('а')
alphabet = list(''.join([chr(i) for i in range(a,a+32)]))
b = alphabet.copy()
b.append('а')
b.append('б')
b.append('в')
print(b)

# alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'э', 'ю', 'я',]

e = []
result = []
for letter in str:
    if letter == ' ':
        result.append(' ')
    # if letter == 'я':
    #     result.append('в')
    else:
        for index, bukva in enumerate(alphabet):
            if letter == bukva:
                result.append(alphabet[index + 3])

crypto_word = ''.join(result)
print(crypto_word)


result2 = []
for letter in crypto_word:
    if letter == ' ':
        result2.append(' ')
    else:
        for index, bukva in enumerate(alphabet):
            if letter == bukva:
                result2.append(alphabet[index - 3])

orig_word = ''.join(result2)
print(orig_word)






