



num = 121

class Solution:
        def isPalindrome(self, x: int) -> bool:
                a = str(x)
                rev = a[::-1]
                return a == rev

print(Solution.isPalindrome(num, num))

