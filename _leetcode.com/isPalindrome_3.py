


a = 'розаdзор'

half = int(len(a) / 2)
isPalindrome = True
for index in range(0, half):
        if a[index] != a[-(index+1)]:
                isPalindrome = False
                break


print(isPalindrome)
