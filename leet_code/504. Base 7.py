class Solution:
    def convertToBase7(self, num: int) -> str:
        if 0 == num:
            return '0'
        sign = -1 if num < 0 else 1
        num = abs(num)
        out = ''
        while num > 0:
            out += str(num%7)
            num //= 7
        return ('-' if sign == -1 else '') + out[::-1]

