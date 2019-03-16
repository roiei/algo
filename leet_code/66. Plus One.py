class Solution:
    def plusOne(self, digits):
        snum = ''
        for i in range(len(digits)):
            snum += str(digits[i])
        num = int(snum)
        num += 1

        res = []
        snum = str(num)
        for i in range(len(snum)):
            res.append(int(snum[i]))
        return res

digits = [1,2,3]

sol = Solution()
ret = sol.plusOne(digits)
print(ret)