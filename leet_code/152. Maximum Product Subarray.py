import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution(object):
    def maxProduct_es(self, nums):
        if not nums:
            return 0
        ms = float('-inf')
        n = len(nums)
        if 1 == n:
            return nums[0]
        for s in range(n):
            for e in range(s+1, n+1):
                print(s, e)
                tot = 1
                for i in range(s, e):
                    tot *= nums[i]
                ms = max(tot, ms)
        return ms

    def maxProduct_ref(self, nums) -> int:
        if not nums:
            return 0
        n = len(nums)
        if 1 == n:
            return nums[0]
        pro_max = [0]*n
        pro_min = [0]*n
        pro_max[0] = pro_min[0] = nums[0]
        for i in range(1, n):
            fmax = pro_max[i-1]*nums[i]
            fmin = pro_min[i-1]*nums[i]
            pro_max[i] = max(nums[i], fmax, fmin)
            pro_min[i] = min(nums[i], fmax, fmin)

        return max(pro_max)

    def maxProduct(self, nums: [int]) -> int:
        if not nums:
            return 0
        
        n = len(nums)
        pmax = pmin = nums[0]
        
        res = [nums[0]]
        for i in range(1, n):
            pro_max = pmax*nums[i]
            pro_min = pmin*nums[i]
            pmax = max(nums[i], pro_max, pro_min)
            pmin = min(nums[i], pro_max, pro_min)
            res += pmax,
            
        return max(res)

    def maxProduct(self, nums: [int]) -> int:
        mx = 0
        cur = 1

        for num in nums:
            cur = max(cur*num, num)
            mx = max(mx, cur)

        print(mx)
        return mx


stime = time.time()
#print(6 == Solution().maxProduct([2,3,-2,4]))
print(108 == Solution().maxProduct_ref([-1,-2,-9,-6]))
print()
print(108 == Solution().maxProduct([-1,-2,-9,-6]))


print('elapse time: {} sec'.format(time.time() - stime))