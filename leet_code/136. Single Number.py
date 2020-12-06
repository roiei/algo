

class Solution:
    def singleNumber(self, nums):
        res = 0
        for num in nums:
            res ^= num
        return res


stime = time.time()
print(1 == Solution().singleNumber([2,2,1]))
print(4 == Solution().singleNumber([4,1,2,1,2]))
