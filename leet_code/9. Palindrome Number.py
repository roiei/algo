
class Solution:
    def isPalindrome(self, x: 'int') -> 'bool':
        num = []
        if x < 0:
            return False
        while x > 0:
            num.append(x%10)
            x //= 10
        n = len(num)
        for i in range(n//2):
            if num[i] != num[n-1-i]:
                return False
        return True

    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        return x == x[::-1]
