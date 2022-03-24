
num = 121

class Solution:
        def revert(self, x):
                x_ = str(x)
                return int(x_[::-1])

        def isPalindrome(self, x: int) -> bool:
                res = (x == Solution.revert(x, x)) if (x > 0) else False
                return res


print(Solution.isPalindrome(num, num))



