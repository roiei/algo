class Solution:
    def isPalindrome(self, x: 'int') -> 'bool':
        if str(x) == str(x)[::-1]:
            return True
        return False



x = 121
x = 10
sol = Solution()
print(sol.isPalindrome(x))
