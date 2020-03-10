
import time
import copy
import collections


class Solution(object):
    def totalHammingDistance_es(self, nums):
        if not nums:
            return 0
        def dfs(num, nums):
            if not nums:
                return 0
            cnt = 0
            for i in range(len(nums)):
                cnt += bin(num^nums[i]).count('1')
            cnt += dfs(nums[0], nums[1:])
            return cnt
        return dfs(nums[0], nums[1:])

    def totalHammingDistance(self, nums):
        if not nums:
            return 0
        cnt = 0
        m = max(nums)
        i = 0
        while (1<<i) <= m:
            ones = zeros = 0
            for num in nums:
                if num&(1<<i):
                    ones += 1
                else:
                    zeros += 1
            cnt += ones*zeros
            i += 1
        return cnt


stime = time.time()
#print(Solution().totalHammingDistance([4, 14, 2]))
print(Solution().totalHammingDistance([4,2,3,2,4]))
print('elapse time: {} sec'.format(time.time() - stime))


