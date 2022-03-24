
num = 121

class Solution:
        def revert(self, x):
                x_ = str(x)
                return int(x_[::-1])

        def isPalindrome(self, x: int) -> bool:
                if x > 0:
                        return x == Solution.revert(x, x)
                else:
                        return False


print(Solution.isPalindrome(num, num))

e = (x == Solution.revert(x, x)) if (x > 0) else False

return e
