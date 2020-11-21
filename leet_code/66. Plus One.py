

class Solution:
    def plusOne(self, digits):
        snum = ''.join([str(digit) for digit in digits])
        return list(map(int, str(int(snum) + 1)))

    def plusOne(self, digits: List[int]) -> List[int]:
        num = ''.join([str(digit) for digit in digits])
        n = len(num)
        num = str(int(num) + 1)
        if len(num) < n:
            num = '0'*(n - len(num)) + num
        return [int(digit) for digit in num]


digits = [1,2,3]

sol = Solution()
ret = sol.plusOne(digits)
print(ret)