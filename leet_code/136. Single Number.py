

class Solution:
    def singleNumber(self, nums):
        res = 0
        for num in nums:
            res ^= num
        return res


stime = time.time()
print(Solution().singleNumber([2,2,1]))
print(Solution().singleNumber([4,1,2,1,2]))
