class Solution:
    def plusOne(self, digits):
        snum = ''.join([str(digit) for digit in digits])
        return list(map(int, str(int(snum) + 1)))

digits = [1,2,3]

sol = Solution()
ret = sol.plusOne(digits)
print(ret)